from django.conf.urls import patterns, include, url
#from django.contrib.auth.views import login, logout

urlpatterns = patterns('cinema.views',
	url(r'^main/$', 'index', name="index"),
	url(r'^main/(\d{1,3})/$', 'post', name="post"),
	url(r'^main/search/$', 'search', name="search"),
	url(r'^$', 'like', name="like"),
)

urlpatterns += patterns('cinema.user_register',
	url(r'^login/reg/$', 'registration', name='reg'),
	url(r'^login/auth/$', 'login', name='log'),
	url(r'^$', 'logout', name='logout'),
)