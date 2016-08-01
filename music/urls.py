from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	#/music/
	url(r'^$', views.Index.as_view(), name='index'),

	#/music/register/
	url(r'^register/$', views.UserFormView.as_view(), name='register'),

	#/music/6559/
	url(r'^(?P<pk>[0-9]+)/$', views.Details.as_view(), name='details'),

	# music/album/add/
	url(r'album/add/$', views.AddAlbum.as_view(), name='add-album'),

	# music/album/update/2/
	url(r'album/update/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='update-album'),

	# music/album/2/delete
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='delete-album'),
	# #/music/6559/favorite
	# url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]