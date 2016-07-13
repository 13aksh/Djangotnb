from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	html = "This is the first page<br>"
	for album in all_albums:
		url = '/music/' + str(album.id) + '/'
		html += "<a href='" + url + "'>" + album.album_title + " - " + album.artist + "</a><br>"
	return HttpResponse(html)

def details(request, album_id):
	html = "<h1>This is Album no. : " + str(album_id) + "</h1>"
	return HttpResponse(html)

