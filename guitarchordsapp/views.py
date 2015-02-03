from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.http import HttpResponse
import django.db
import MySQLdb
import re
import urllib
import urllib2
import sys
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render_to_response, RequestContext, Http404, get_object_or_404
from guitarchordsapp.forms import doyouknowForm
from guitarchordsapp.models import doyouknow
# Create your views here.

###adding a new function to capture views in the home page
def catalog(request):
	#my_context = context({ 'name': 'GC' })
	name = 'Gc'
	#return HttpResponse(response_html)
	db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	#cursor.execute("SELECT VERSION()")
	#cursor.execute("DROP TABLE IF EXISTS employee")
	# Create table as per requirement
	sql = """select CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and language = 'hindi' and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()

	hin_songname = [row[0] for row in rows]
	hin_songviews = [row[1] for row in rows]
	hin = zip(hin_songname , hin_songviews)
	#hin = []
	#hin.append(hin_songname)
	#hin.append(hin_songviews)

	#englishsong name
	sql1 = """select artist_name, CONCAT(albumname,' - ',song_name) , views from gc_fact_userchords
	where uploaded_by = 'admin' and language = 'english' and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql1)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	engrows = cursor.fetchall()
	eng_artistname = [row[0] for row in engrows]

	eng_songname = [row[1] for row in engrows]
	eng_songviews = [row[2] for row in engrows]
	eng = zip(eng_artistname, eng_songname , eng_songviews)

	#Tamil

	sql_tam = """select CONCAT(albumname,' - ',song_name), IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and language = 'tamil' and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql_tam)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	tamrows = cursor.fetchall()

	tam_songname = [row[0] for row in tamrows]
	tam_songviews = [row[1] for row in tamrows]
	tam = zip(tam_songname , tam_songviews)

	#Kannada

	sql_kan = """select CONCAT(albumname,' - ',song_name), IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and language = 'kannada' and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql_kan)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	kanrows = cursor.fetchall()

	kan_songname = [row[0] for row in kanrows]
	kan_songviews = [row[1] for row in kanrows]
	kan = zip(kan_songname , kan_songviews)

	#Telugu
	sql_tel = """select CONCAT(albumname,' - ',song_name), IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and (language = 'telgu' or language = 'telugu') and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql_tel)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	telrows = cursor.fetchall()

	tel_songname = [row[0] for row in telrows]
	tel_songviews =[row[1] for row in telrows]
	tel = zip(tel_songname , tel_songviews)

	#bangla
	sql_bangla = """select CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and language = 'bangla' and gvsng = 'non-gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 10;
	"""

	cursor.execute(sql_bangla)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	banglarows = cursor.fetchall()

	bangla_songname = [row[0] for row in banglarows]
	bangla_songviews = [row[1] for row in banglarows]
	bangla = zip(bangla_songname, bangla_songviews)

	#popular gospel
	sql_gsp = """select artist_name, CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
	where uploaded_by = 'admin' and gvsng = 'gospel'
	ORDER BY IFNULL(views,0) DESC LIMIT 9;
	"""

	cursor.execute(sql_gsp)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_gsp = cursor.fetchall()

	gospel_artistname = [row[0] for row in rows_gsp]
	gospel_songname = [row[1] for row in rows_gsp]
	gospel_songviews = [row[2] for row in rows_gsp]
	gospel = zip( gospel_songname, gospel_songviews)
		#data = cursor.fetchall()
	#data = str(data).replace('),',"|").replace("(('","").replace("'","").replace(",","").replace("))","").replace("( ","").strip()

	#data = data.split("|")
		#print "Database version : %s " % data
	d = 'language'
	hin_lang = 'hindi'
	eng_lang = 'english'
	tam_lang = 'tamil'
	kan_lang = 'kannada'
	bangla_lang = 'bangla'
	tel_lang = 'telugu'
	return render_to_response('index.html', {'eng':eng,'hin':hin, 'tel':tel, 'tam':tam, 'kan':kan,
	'bangla':bangla, 'gospel':gospel, 'hin_lang':hin_lang, 'eng_lang':eng_lang, 'tam_lang':tam_lang, 'kan_lang':kan_lang,
	'tel_lang':tel_lang, 'bangla_lang':bangla_lang, 'd':d })

#not in use
def catalog_v(request):
	#my_context = context({ 'name': 'GC' })
	name = 'Gc'
	#return HttpResponse(response_html)

	db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	#cursor.execute("SELECT VERSION()")
	#cursor.execute("DROP TABLE IF EXISTS employee")
	# Create table as per requirement
	sql = """select CONCAT(song_name," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'hindi'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()

	hin_songname = [row[0] for row in rows]


    #englishsong name
	sql1 = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'english'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql1)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	engrows = cursor.fetchall()

	eng_songname = [row[0] for row in engrows]
    #Tamil

	sql_tam = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'tamil'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql_tam)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	tamrows = cursor.fetchall()

	tam_songname = [row[0] for row in tamrows]


    #Kannada

	sql_kan = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'kannada'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql_kan)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	kanrows = cursor.fetchall()

	kan_songname = [row[0] for row in kanrows]

    #Telugu
	sql_tel = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'telugu'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql_tel)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	telrows = cursor.fetchall()

	tel_songname = [row[0] for row in telrows]

    #bangla
	sql_bangla = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'banglail'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql_bangla)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	banglarows = cursor.fetchall()

	bangla_songname = [row[0] for row in banglarows]


    #popular gospel
	sql_gsp = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and songcategory = 'gospel'
	ORDER BY RAND() LIMIT 9;
	"""

	cursor.execute(sql_gsp)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_gsp = cursor.fetchall()

	gospel_songname = [row[0] for row in rows_gsp]


		#data = cursor.fetchall()
	#data = str(data).replace('),',"|").replace("(('","").replace("'","").replace(",","").replace("))","").replace("( ","").strip()

	#data = data.split("|")
		#print "Database version : %s " % data
	d = 'language'
	hin_lang = 'hindi'
	eng_lang = 'english'
	tam_lang = 'tamil'
	kan_lang = 'kannada'
	bangla_lang = 'bangla'
	tel_lang = 'telugu'
	return render_to_response('index.html', {'engname':eng_songname,
		'hin_songname':hin_songname, 'tel_songname':tel_songname, 'tam_songname':tam_songname, 'kan_songname':kan_songname,
		'bangla_songname':bangla_songname, 'gospel_songname':gospel_songname,
		 'hin_lang':hin_lang, 'eng_lang':eng_lang, 'tam_lang':tam_lang, 'kan_lang':kan_lang, 'tel_lang':tel_lang, 'bangla_lang':bangla_lang, 'd':d})

def search(request):
    query = request.GET['q']
    likequery = "%"+str(query)+"%"
    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #english
    sql1 = ("""select CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
    where MATCH(song_name,albumname,artist_name) AGAINST('%s') ORDER BY albumname """ %query)

    cursor.execute(sql1)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    engrows = cursor.fetchall()

    songname = [row[0] for row in engrows]
    songviews = [row[1] for row in engrows]
    song = zip( songname, songviews)
    #like matching
    #hillsong vs hillsongs
    sql2 = ("""select distinct CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
    where albumname LIKE '%s' or song_name LIKE '%s' ORDER BY albumname""" %(likequery, likequery))


    cursor.execute(sql2)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    likerows = cursor.fetchall()

    like_songname = [row[0] for row in likerows]
    like_songviews = [row[1] for row in likerows]
    like_song = zip( like_songname, like_songviews)


    return render_to_response('search_page.html',{ 'song':song,'like_song':like_song,	})


def vsearch(request):
    query = request.GET['q']
    youtube_query = "how to play "+str(query)+" on guitar"
    youtube_q = str(youtube_query).replace(" ",'+')
    resp = urllib2.urlopen('https://www.youtube.com/results?search_query='+str(youtube_q))
    content = resp.read()
    links = re.findall('(?<=["][/]watch[?]v[=]).+?(?=["])',str(content))
    embeds = []
    for actlinks in links:
    	embeds.append(str(actlinks))

    link1 = embeds[1]
    link2 = embeds[3]
    link3 = embeds[5]
    link4 = embeds[7]
    link5 = embeds[9]
    return render_to_response('vsearch.html',{ 'link1':link1, 'link2':link2, 'link3':link3, 'link4':link4, 'link5':link5})

def guitar_chords(request):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0-9']
    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("""select  CONCAT(albumname,' - ',song_name) , IFNULL(views,0) from gc_fact_userchords
    where language = 'hindi' and gvsng = 'non-gospel'	ORDER BY RAND() LIMIT 15;""" )
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()


    song_name = [row[0] for row in rows]
    song_views = [row[1] for row in rows]
    hin_songs = zip(song_name , song_views)

    #english
    sql1 = """select artist_name, CONCAT(albumname,' - ',song_name) , IFNULL(views ,0) from gc_fact_userchords
    where language = 'english' and gvsng = 'non-gospel'	ORDER BY RAND() LIMIT 15;
    """

    cursor.execute(sql1)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    engrows = cursor.fetchall()
    eng_artistname = [row[0] for row in engrows]
    eng_songname = [row[1] for row in engrows]
    eng_songviews = [row[2] for row in engrows]
    eng_songs = zip(eng_artistname, eng_songname, eng_songviews)

    #regional
    sql2 = """select  CONCAT(albumname,' - ',song_name), IFNULL(views ,0) from gc_fact_userchords
    where language <> 'hindi' and language <> 'english' and gvsng = 'non-gospel' ORDER BY RAND() LIMIT 15;
    """

    cursor.execute(sql2)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    regrows = cursor.fetchall()


    reg_songname = [row[0] for row in regrows]
    reg_songviews = [row[1] for row in regrows]
    reg_songs = zip( reg_songname, reg_songviews)

    return render_to_response('guitar_chords.html',{'alpha':alpha, 'hin_songs':hin_songs, 'eng_songs':eng_songs,'reg_songs':reg_songs})


def guitar_chords_v(request):
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = ("""select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'hindi'
	ORDER BY RAND() LIMIT 15;""" )
	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()

	song_name = [row[0] for row in rows]

	#english
	sql1 = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'english'
	ORDER BY RAND() LIMIT 15;
	"""

	cursor.execute(sql1)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	engrows = cursor.fetchall()

	eng_songname = [row[0] for row in engrows]

    #regional
	sql2 = """select CONCAT(songname," - ",albumname) from userchords
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category <> 'hindi' and category <> 'english'
	ORDER BY RAND() LIMIT 15;
	"""

	cursor.execute(sql2)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	regrows = cursor.fetchall()

	reg_songname = [row[0] for row in regrows]


	return render_to_response('guitar_chords.html',{'alpha':alpha, 'song_name':song_name, 'eng_songname':eng_songname,'reg_songname':reg_songname})

def learn_guitar(request):
	return render_to_response('learn_guitar.html')

def learn_guitar_chords(request):
	return render_to_response('learn_guitar_chords.html')

def learn_more_guitar_chords(request):
	return render_to_response('learn_more_guitar_chords.html')

def upload_guitar_chords(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('upload_guitar_chords.html',c)

def capture_guitar_chords(request):
    c = {}
    c.update(csrf(request))
    username = str(request.POST.get('username'))
    song_release_date = str(request.POST.get('datepicker'))
    song_name = str(request.POST.get('song_name')).replace("'","").replace('"',"")
    language = str(request.POST.get('mydropdown'))
    gvsng = str(request.POST.get('mydropdown_0'))
    albumname =str(request.POST.get('albumname')).replace("'","").replace('"',"")
    artist_name =str(request.POST.get('artist_name')).replace("'","").replace('"',"")
    guitarchords =str(request.POST.get('guitarchords')).replace("'"," ").replace('"'," ").replace("-"," ").replace("...","   ")


    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    checksong_avail  = (""" select song_name from gc_fact_userchords where song_name = '%s' and albumname = '%s' and artist_name = '%s' """ %(song_name , albumname, artist_name))
    cursor.execute(checksong_avail)
    checkrows = cursor.fetchall()
    check_songname = [row[0] for row in checkrows]
    if (song_release_date == None or song_name  == '' or albumname == '' or artist_name == '' or guitarchords==''):
        return render_to_response('enterrequiredfield.html', {'song_release_date':song_release_date, 'song_name':song_name, 'albumname':albumname, 'artist_name':artist_name  ,})
    elif check_songname:
        from twilio.rest import TwilioRestClient
        #import twilio
        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = "ACeeb499cfa1ff7b58d3e964e4715608e6"
        auth_token = "f89e557359f4da84536f4ffb4bb65826"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.sms.messages.create(body="%s is trying to upload a song - %s - %s that is already present in guitarclub.in" %(username,song_name, albumname),
        to="+919740802044",
        from_="+13343709574")
        print message.sid
        return render_to_response('songexists.html', {'username':username, 'song_name':song_name, 'albumname':albumname , 'song_release_date':song_release_date})
    else:
        sql = ("""INSERT INTO gc_fact_userchords(song_release_date, song_name , albumname, artist_name , language , gvsng , chords, uploaded_by)
        VALUES('%s','%s','%s','%s','%s','%s','%s', 'Admin')"""%(song_release_date, song_name ,albumname, artist_name, language , gvsng, guitarchords))
        cursor.execute(sql)
        db.commit()
        from twilio.rest import TwilioRestClient
        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = "ACeeb499cfa1ff7b58d3e964e4715608e6"
        auth_token = "f89e557359f4da84536f4ffb4bb65826"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.sms.messages.create(body="%s has uploaded a song - %s - %s into guitarclub.in" %(username,song_name, albumname),
        to="+919740802044",
        from_="+13343709574")
        print message.sid
        return render_to_response('thankyou.html', {'username':username, 'song_name':song_name, 'albumname':albumname, 'song_release_date':song_release_date})

def video_guitar_lessons(request):
	return render_to_response('video_guitar_lessons.html')

def gospel_guitar_page(request):
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
	db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql_e = ("""select  artist_name, CONCAT(albumname,' - ',song_name),IFNULL(views,0)  from gc_fact_userchords
	where LOWER(gvsng) ='gospel' and LOWER(language) = 'english'
	ORDER BY artist_name , albumname """)
	cursor.execute(sql_e)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()

	artist_name_e = [row[0] for row in rows]
	song_name_e = [row[1] for row in rows]
	song_views_e = [row[2] for row in rows]
	songs_e = zip(artist_name_e, song_name_e , song_views_e)

	sql_h = ("""select  CONCAT(albumname,' - ',song_name), IFNULL(views,0)   from gc_fact_userchords
	where gvsng ='gospel' and LOWER(language) = 'hindi'
	ORDER BY albumname """)

	cursor.execute(sql_h)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_h = cursor.fetchall()

	song_name_h = [row[0] for row in rows_h]
	song_views_h = [row[1] for row in rows_h]
	songs_h =zip(song_name_h, song_views_h)

	sql_r = ("""select  CONCAT(albumname,' - ',song_name) , IFNULL(views,0)  from gc_fact_userchords
	where gvsng ='gospel' and (LOWER(language) <> 'hindi' and LOWER(language) <> 'english')
	ORDER BY albumname """	)
	cursor.execute(sql_r)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_r = cursor.fetchall()

	song_name_r = [row[0] for row in rows_r]
	song_views_r = [row[1] for row in rows_r]
	songs_r = zip(song_name_r , song_views_r)


	return render_to_response('gospel_guitar_page.html',{'alpha':alpha, 'songname_e':songs_e,'songname_h':songs_h,'songname_r':songs_r})

def gospel_alpha_page(request, d):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
    songname = str(d)+"%"
    if songname == '0-9':
        regex_songname = '^-?[0-9]+$'
        db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
        where gvsng = 'gospel' and albumname REGEXP '%s' GROUP BY artist_name, albumname""" %regex_songname)
        cursor.execute(sql)
        # Fetch a single row using fetchone() method.
        #fetch all rows
        rows = cursor.fetchall()
        artistname = [row[0] for row in rows]
        albumname = [row[1] for row in rows]
        albumviews = [row[2] for row in rows]
        album = zip(artistname, albumname,albumviews)
        return render_to_response('gospel_alpha_page.html',{'alpha':alpha, 'albumname':album})
    else:
        db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
        where gvsng = 'gospel' and (albumname like '%s' or artist_name like '%s') GROUP BY artist_name, albumname""" %(songname, songname))
        cursor.execute(sql)
        # Fetch a single row using fetchone() method.
        #fetch all rows
        rows = cursor.fetchall()
        artistname = [row[0] for row in rows]
        albumname = [row[1] for row in rows]
        albumviews = [row[2] for row in rows]
        album = zip(artistname, albumname,albumviews)
        return render_to_response('gospel_alpha_page.html',{'alpha':alpha, 'albumname':album})



def gospel_guitarsongs(request, d):
    songname = str(d)
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("""select  CONCAT(albumname,' - ',song_name), IFNULL(views ,0) from gc_fact_userchords
    where gvsng = 'gospel' and albumname ='%s' ORDER BY albumname""" %songname)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    song_name = [row[0] for row in rows]
    song_views = [row[1] for row in rows]
    songs = zip(song_name , song_views)
    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('gospel_guitarsongs.html',{'albumname':songname,'song_name':songs,'alpha':alpha})


def gospel_guitarsongs_v(request, d):
    songname = str(d)
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$testdb" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("""select  CONCAT(songname," - ",albumname) from userchords
    where albumname ='%s'""" %songname)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    song_name = [row[0] for row in rows]

    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('gospel_guitarsongs.html',{'albumname':songname,'song_name':song_name,'alpha':alpha})

def gospel_guitarchords(request, d):
    songname = str(d)

    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
        ##update the number of views in the database
    sqlupdate = ("""UPDATE gc_fact_userchords SET views = views+1
    	where CONCAT(albumname,' - ',song_name) = '%s'"""%songname)
    cursor.execute(sqlupdate)
    db.commit()

    sql = ("""select songid, chords , views  from gc_fact_userchords
    where CONCAT(albumname,' - ',song_name) ='%s'""" %songname)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    song_id = [row[0] for row in rows]
    chords = [row[1] for row in rows]
    chord_views = [row[2] for row in rows]



    ## get the comments section
    #sql_com = ("""select comments , commented_by from gc_fact_commments
    #where song_id ='%s'""" %song_id)
    #cursor.execute(sql_com)
    #row = cursor.fetchall()

    #comments = [row[0] for row in rows]
    #commented_by = [row[1] for row in rows]
    #comm = zip(comments , commented_by)

    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('gospel_guitarchords.html',{'songname':songname,'chords':chords,'chord_views':chord_views})


def gospel_guitarchords_v(request, d):
    songname = str(d)

    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$testdb" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("""select chords from userchords
    where CONCAT(songname," - ",albumname) ='%s'""" %songname)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    chords = [row[0] for row in rows]

    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('gospel_guitarchords.html',{'songname':songname,'chords':chords})

def guitar_alpha_page(request, d):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0-9']
    #if the alpha request is not coming from guitar chords page then do not alow the user to search all the languages
    if re.search(r'[/]', str(d)):
        songlist = str(d).split('/')
        alpha_clicked = str(songlist[0])+"%"

        language = str(songlist[1])
        if language <> 'ALL':
            if alpha_clicked == '0-9%':
                alpha_clicked_num = '^-?[0-9]+$'
                db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
                where gvsng = 'non-gospel' and (albumname REGEXP '%s' or artist_name REGEXP '%s') and LOWER(language) = '%s' GROUP BY albumname ORDER BY IFNULL(views,0) DESC """ %(alpha_clicked_num,alpha_clicked_num,language))

                cursor.execute(sql)
                # Fetch a single row using fetchone() method.
                #fetch all rows
                rows = cursor.fetchall()

                artistname = [row[0] for row in rows]
                albumname = [row[1] for row in rows]
                albumviews = [row[2] for row in rows]
                album = zip(artistname, albumname , albumviews)

            else:
                db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
                where gvsng = 'non-gospel' and (albumname LIKE '%s' or artist_name LIKE '%s') and LOWER(language) = '%s' GROUP BY albumname ORDER BY IFNULL(views,0) DESC""" %(alpha_clicked,alpha_clicked, language))

                cursor.execute(sql)
                # Fetch a single row using fetchone() method.
                #fetch all rows
                rows = cursor.fetchall()

                artistname = [row[0] for row in rows]
                albumname = [row[1] for row in rows]
                albumviews = [row[2] for row in rows]
                album = zip(artistname, albumname , albumviews)
        else:
            if alpha_clicked == '0-9%':
                alpha_clicked_num = '^-?[0-9]+$'
                db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                sql = ("""select  artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
                where gvsng = 'non-gospel' and (albumname REGEXP '%s'or artist_name REGEXP '%s') GROUP BY albumname ORDER BY IFNULL(views,0) DESC """ %(alpha_clicked_num,alpha_clicked_num))

                cursor.execute(sql)
                # Fetch a single row using fetchone() method.
                #fetch all rows
                rows = cursor.fetchall()
                artistname = [row[0] for row in rows]
                albumname = [row[1] for row in rows]
                albumviews = [row[2] for row in rows]
                album = zip(artistname, albumname , albumviews)
                language= "ALL"

            else:
                db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

                # prepare a cursor object using cursor() method
                cursor = db.cursor()
                sql = ("""select  artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
                where gvsng = 'non-gospel' and (albumname LIKE '%s' or artist_name LIKE '%s') GROUP BY albumname ORDER BY IFNULL(views,0) DESC """ %(alpha_clicked,alpha_clicked))

                cursor.execute(sql)
                # Fetch a single row using fetchone() method.
                #fetch all rows
                rows = cursor.fetchall()

                artistname = [row[0] for row in rows]
                albumname = [row[1] for row in rows]
                albumviews = [row[2] for row in rows]
                album = zip(artistname, albumname , albumviews)
                language= "ALL"
    else:
        songlist = str(d)
        alpha_clicked = str(songlist)+"%"
        if alpha_clicked == '0-9%':
            alpha_clicked_num = '^-?[0-9]+$'
            #alpha_clicked_num = '^[0-9]'
            db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
            where gvsng = 'non-gospel' and (albumname REGEXP '%s' or artist_name REGEXP '%s') GROUP BY albumname ORDER BY IFNULL(views,0) DESC""" %(alpha_clicked_num,alpha_clicked_num))

            cursor.execute(sql)
            # Fetch a single row using fetchone() method.
            #fetch all rows
            rows = cursor.fetchall()
            artistname = [row[0] for row in rows]
            albumname = [row[1] for row in rows]
            albumviews = [row[2] for row in rows]
            album = zip(artistname, albumname , albumviews)
            language= "ALL"


        else:
            db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            sql = ("""select artist_name, albumname, SUM(IFNULL(views,0)) from gc_fact_userchords
            where gvsng = 'non-gospel' and (albumname LIKE '%s' or artist_name LIKE '%s') GROUP BY albumname ORDER BY IFNULL(views,0) DESC""" %(alpha_clicked,alpha_clicked))

            cursor.execute(sql)
            # Fetch a single row using fetchone() method.
            #fetch all rows
            rows = cursor.fetchall()

            artistname = [row[0] for row in rows]
            albumname = [row[1] for row in rows]
            albumviews = [row[2] for row in rows]
            album = zip(artistname, albumname , albumviews)

            language= "ALL"

    return render_to_response('guitar_alpha_page.html',{'alpha':alpha, 'albumname':album,'language':language})

def privacy(request):
    return render_to_response('GuitarClubprivacy.html')

def artist_guitarsongs(request, d):
    songname = str(d)
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("""select  CONCAT(albumname,' - ',song_name), IFNULL(views,0) from gc_fact_userchords
    where albumname ='%s'""" %songname)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    song_name = [row[0] for row in rows]
    song_views = [row[1] for row in rows]
    songs = zip(song_name , song_views)
    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('artist_guitarsongs.html',{'albumname':songname,'song_name':songs,'alpha':alpha})

def det_guitarchords(request, d):
    songname = str(d)

    db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #sql = ("""select chords from gc_fact_userchords
    #where CONCAT(song_name," - ",albumname) ='%s' or songname = '%s'""" %(songname , songname))
    #cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    #rows = cursor.fetchall()

    #chords = [row[0] for row in rows]
    sqlupdate = ("""UPDATE gc_fact_userchords SET views = views+1
    	where CONCAT(albumname,' - ',song_name) ='%s'""" %songname)
    cursor.execute(sqlupdate)
    db.commit()

    sql = ("""select albumname , chords , views  from gc_fact_userchords
    where CONCAT(albumname,' - ',song_name) ='%s'or song_name = '%s'""" %(songname , songname))
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    #fetch all rows
    rows = cursor.fetchall()

    albumname = [row[0] for row in rows]
    chords = [row[1] for row in rows]
    chord_views = str([row[2] for row in rows])

    ##update the number of views in the database




    ## get the comments section
    #sql_com = ("""select comments , commented_by from gc_fact_commments
    #where song_id ='%s'""" %song_id)
    #cursor.execute(sql_com)
    #row = cursor.fetchall()

    #comments = [row[0] for row in rows]
    #commented_by = [row[1] for row in rows]
    #comm = zip(comments , commented_by)

    #msg= get_object_or_404(Post,slug=d)
    return render_to_response('det_guitarchords.html',{'songname':songname,'chords':chords, 'chord_views':chord_views})

def more_guitarsongs(request, d):
    lang_selected = str(d).split('/')
    language = str(lang_selected[1])
    if language == 'english':
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
        db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = ("""select artist_name, CONCAT(albumname,' - ',song_name), IFNULL(views,0)from gc_fact_userchords
        where gvsng = 'non-gospel' and LOWER(language) = '%s'
        ORDER BY artist_name, albumname;
        """ %language)
        cursor.execute(sql)
        # Fetch a single row using fetchone() method.
        #fetch all rows
        rows = cursor.fetchall()
        artistname = [row[0] for row in rows]
        songname = [row[1] for row in rows]
        songviews = [row[2] for row in rows]
        songs = zip(artistname, songname , songviews)
        return render_to_response('more_guitar_songs_eng.html',{'songname':language, 'alpha':alpha , 'language':language, 'songs':songs})

    else:
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0-9']
        db = MySQLdb.connect("mysql.server","pakumar","P@ssw0rd","pakumar$dm_gc" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = ("""select CONCAT(albumname,' - ',song_name), IFNULL(views,0)from gc_fact_userchords
        where gvsng = 'non-gospel' and LOWER(language) = '%s'
        ORDER BY albumname;
        """ %language)
        cursor.execute(sql)
        # Fetch a single row using fetchone() method.
        #fetch all rows
        rows = cursor.fetchall()

        #change the order to show album name only for hindi songs
        songname = [row[0] for row in rows]
        songviews = [row[1] for row in rows]
        songs = zip(songname , songviews)

        return render_to_response('more_guitar_songs.html',{'songname':language, 'alpha':alpha , 'language':language, 'songs':songs})

def fb(request):
    return render_to_response('fb.html', {'doyouknow': doyouknow.objects.all().order_by('update_number').reverse() })

def fbm(request):
    return render_to_response('fbm.html', {'doyouknow': doyouknow.objects.all().order_by('update_number').reverse() })


def fb_share(request, doyouknow_id=1):
    return render_to_response('fb_share.html', {'doyouknow':doyouknow.objects.get(id = doyouknow_id)}  )

def xmas(request):
    return render_to_response('theme_christmas.html')

def upload_doyouknow(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('upload_doyouknow.html',c)

def capture_doyouknow(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        form = doyouknowForm(request.POST , request.FILES)
        #if form.is_valid():
        form.save()
        return render_to_response('upload_doyouknow.html',c)
        #else:
         #  return render_to_response('theme_christmas.html')
    else:
        return render_to_response('fb_share.html')

    #fbposts = request.POST.get('fileField')
    #newfile = open('fbpost', 'w')
    #newfile.write('/home/pakumar/GuitarClub/guitarchordsapp/static/')
    #return ("successful")

def editor(request):
    return render_to_response('editor.html')

def mcatalog(request):
    return render_to_response('mindex.html')

def republic(request):
    return render_to_response('theme_republic.html')





