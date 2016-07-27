from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	#/music/
	url(r'^$', views.Index.as_view(), name='index'),

	#/music/6559/
	url(r'^(?P<pk>[0-9]+)/$', views.Details.as_view(), name='details'),

	# music/album/add/
	url(r'album/add/$', views.AddAlbum.as_view(), name='add-album')
	# #/music/6559/favorite
	# url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]