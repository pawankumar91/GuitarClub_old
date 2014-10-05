from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
from django.http import HttpResponse
import django.db
import MySQLdb
import re
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render_to_response, RequestContext, Http404, get_object_or_404

# Create your views here.

def catalog(request):
	#my_context = context({ 'name': 'GC' })
	name = 'Gc'
	#return HttpResponse(response_html)
	
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	#cursor.execute("SELECT VERSION()")
	#cursor.execute("DROP TABLE IF EXISTS employee")
	# Create table as per requirement
	sql = """select CONCAT(songname," - ",albumname) from userchords
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
	where email = 'admin.pawan.kumar.13.1991@gmail.com' and category = 'telil'
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
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
#english
	sql1 = ("""select CONCAT(songname," - ",albumname) from userchords
	where MATCH(songname,albumname) AGAINST('%s') """ %query)
	
			 
	cursor.execute(sql1)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	engrows = cursor.fetchall()
	
	songname = [row[0] for row in engrows]
#like matching
#hillsong vs hillsongs
	sql2 = ("""select distinct CONCAT(songname," - ",albumname) from userchords
	where albumname LIKE '%s' """ %likequery)
	
		 
	cursor.execute(sql2)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	likerows = cursor.fetchall()
	
	like_songname = [row[0] for row in likerows]
	
	
	return render_to_response('search_page.html',{ 'songname':songname,
'like_songname':like_songname,	})	
		
def guitar_chords(request):
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

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
	name = str(request.POST.get('first_name'))
	email = str(request.POST.get('email'))
	songname = str(request.POST.get('songname')).replace("'","").replace('"',"")
	songcategory = str(request.POST.get('mydropdown_0'))
	category = str(request.POST.get('mydropdown'))
	albumname =str(request.POST.get('albumname')).replace("'","").replace('"',"")
	guitarchords =str(request.POST.get('guitarchords')).replace("'","").replace('"',"")


	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = ("""INSERT INTO userchords( name , email , songname ,songcategory, category, albumname, chords)
	VALUES('Pawan','admin.pawan.kumar.13.1991@gmail.com','%s','%s','%s','%s','%s')"""%(songname ,songcategory, category, albumname , guitarchords))
	cursor.execute(sql)
	db.commit()

	return render_to_response('thankyou.html', {'name':name, 'songname':songname, 'albumname':albumname,'category':category, 'chords':guitarchords})

def video_guitar_lessons(request):
	return render_to_response('video_guitar_lessons.html')

def gospel_guitar_page(request):
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql_e = ("""select  CONCAT(songname," - ",albumname)  from userchords
	where songcategory ='gospel' and category = 'english' 
	ORDER BY RAND() LIMIT 10 """
	)
	cursor.execute(sql_e)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()
	
	song_name_e = [row[0] for row in rows]
	
	sql_h = ("""select  CONCAT(songname," - ",albumname)   from userchords
	where songcategory ='gospel' and category = 'hindi' 
	ORDER BY RAND() LIMIT 10 """
	)
	cursor.execute(sql_h)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_h = cursor.fetchall()
	
	song_name_h = [row[0] for row in rows_h]

	sql_r = ("""select  CONCAT(songname," - ",albumname)   from userchords
	where songcategory ='gospel' and (category <> 'hindi' and category <> 'english') 
	ORDER BY RAND() LIMIT 10 """
	)
	cursor.execute(sql_r)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows_r = cursor.fetchall()
	
	song_name_r = [row[0] for row in rows_r]
	

	return render_to_response('gospel_guitar_page.html',{'alpha':alpha, 'songname_e':song_name_e,'songname_h':song_name_h,'songname_r':song_name_r})

def gospel_alpha_page(request, d):
	songname = str(d)+"%"
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	
	sql = ("""select distinct albumname from userchords
	where songcategory = 'gospel' and albumname LIKE '%s'""" %songname)
	
	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()
	
	album_name = [row[0] for row in rows]

	return render_to_response('gospel_alpha_page.html',{'alpha':alpha, 'albumname':album_name})

	


def gospel_guitarsongs(request, d):
	songname = str(d)
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

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
	
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

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
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#if the alpha request is not coming from guitar chords page then do not alow the user to search all the languages 
	if re.search(r'[/]', str(d)):
		songlist = str(d).split('/')
		alpha_clicked = str(songlist[0])+"%"
		language = str(songlist[1])
		if language <> 'ALL':

			db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			sql = ("""select distinct albumname from userchords
			where songcategory = 'non-gospel' and albumname LIKE '%s' and category = '%s'""" %(alpha_clicked,language))
			
			cursor.execute(sql)
			# Fetch a single row using fetchone() method.
			#fetch all rows
			rows = cursor.fetchall()
			
			
			album_name = [row[0] for row in rows]
		else:
			db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			sql = ("""select distinct albumname from userchords
			where songcategory = 'non-gospel' and albumname LIKE '%s'""" %alpha_clicked)
			
			cursor.execute(sql)
			# Fetch a single row using fetchone() method.
			#fetch all rows
			rows = cursor.fetchall()
			
			album_name = [row[0] for row in rows]	
			language= "ALL"
	else:
		songlist = str(d)
		alpha_clicked = str(songlist)+"%"
		db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		sql = ("""select distinct albumname from userchords
		where songcategory = 'non-gospel' and albumname LIKE '%s'""" %alpha_clicked)
		
		cursor.execute(sql)
		# Fetch a single row using fetchone() method.
		#fetch all rows
		rows = cursor.fetchall()
		
		album_name = [row[0] for row in rows]

		language= "ALL"

	return render_to_response('guitar_alpha_page.html',{'alpha':alpha, 'albumname':album_name,'language':language})

def artist_guitarsongs(request, d):
	songname = str(d)
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

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
	return render_to_response('artist_guitarsongs.html',{'albumname':songname,'song_name':song_name,'alpha':alpha})

def det_guitarchords(request, d):
	songname = str(d)
	
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = ("""select chords from userchords
	where CONCAT(songname," - ",albumname) ='%s' or songname = '%s'""" %(songname , songname))
	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()
	
	chords = [row[0] for row in rows]
	
	#msg= get_object_or_404(Post,slug=d)
	return render_to_response('det_guitarchords.html',{'songname':songname,'chords':chords})

def more_guitarsongs(request, d):
	lang_selected = str(d).split('/')
	language = str(lang_selected[1])
	
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	db = MySQLdb.connect("localhost","pakumar","P@ssw0rd","testdb" )
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = ("""select distinct CONCAT(songname," - ",albumname) from userchords 
	where songcategory = 'non-gospel' and category = '%s'
	ORDER BY RAND() LIMIT 100;
""" %language)
	cursor.execute(sql)
	# Fetch a single row using fetchone() method.
	#fetch all rows
	rows = cursor.fetchall()
	
	songname = [row[0] for row in rows]
	
	return render_to_response('more_guitar_songs.html',{'songname':songname, 'alpha':alpha , 'language':language})
	

