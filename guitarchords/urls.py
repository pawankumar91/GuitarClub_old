from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guitarchords.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^catalog/$', 'guitarchordsapp.views.catalog'),
	url(r'^hindi_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^english_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^tamil_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^bangla_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^kannada_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^telugu_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^gospel_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
		
	url(r'^more_guitarsongs/(?P<d>.*)/$', 'guitarchordsapp.views.more_guitarsongs'),
	
	url(r'^search.*/$', 'guitarchordsapp.views.search'),
	url(r'^guitar_chords/$', 'guitarchordsapp.views.guitar_chords'),
	url(r'^learn_guitar/$', 'guitarchordsapp.views.learn_guitar'),
	url(r'^learn_guitar_chords/$', 'guitarchordsapp.views.learn_guitar_chords'),
	url(r'^learn_more_guitar_chords/$', 'guitarchordsapp.views.learn_more_guitar_chords'),
	url(r'^video_guitar_lessons/$', 'guitarchordsapp.views.video_guitar_lessons'),

	url(r'^upload_guitar_chords/$', 'guitarchordsapp.views.upload_guitar_chords'),
	url(r'^capture_guitar_chords/$', 'guitarchordsapp.views.capture_guitar_chords'),
	url(r'^gospel_guitar_page/$', 'guitarchordsapp.views.gospel_guitar_page'),
	url(r'^gospel_alpha_page/(?P<d>.*)/$', 'guitarchordsapp.views.gospel_alpha_page'),
	url(r'^guitar_alpha_page/(?P<d>.*)/$', 'guitarchordsapp.views.guitar_alpha_page'),
	url(r'^gospel_guitarsongs/(?P<d>.*)/$', 'guitarchordsapp.views.gospel_guitarsongs'),
	url(r'^gospel_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.gospel_guitarchords'),
	url(r'^artist_guitarsongs/(?P<d>.*)/$', 'guitarchordsapp.views.artist_guitarsongs'),
	url(r'^det_guitarchords/(?P<d>.*)/$', 'guitarchordsapp.views.det_guitarchords'),
	url(r'^english_guitarsongs/$', 'guitarchordsapp.views.english_guitarsongs'),
	url(r'^hindi_guitarsongs/$', 'guitarchordsapp.views.hindi_guitarsongs'),
	url(r'^tamil_guitarsongs/$', 'guitarchordsapp.views.tamil_guitarsongs'),
	url(r'^bangla_guitarsongs/$', 'guitarchordsapp.views.bangla_guitarsongs'),
	url(r'^kannada_guitarsongs/$', 'guitarchordsapp.views.kannada_guitarsongs'),
	url(r'^gospel_guitarsongs/$', 'guitarchordsapp.views.gospel_guitarsongs'),
	url(r'^more_gospel_guitarsongs/$', 'guitarchordsapp.views.gospel_guitarsongs'),
)
