from django.shortcuts import render, get_object_or_404
#from django.http import Http404 --> This is not required as we are using get_object_or_404
# Using django.shortcuts import render (For using templates shortcut)
#from django.template import loader

from .models import Album, Song

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	# template = loader.get_template('music/index.html') This is no more required in case we use shortcuts
	context = {
		'all_albums': all_albums
	}
	####### This is the code before using templates#####
	# html = "This is the first page<br>"
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) + '/'
	# 	html += "<a href='" + url + "'>" + album.album_title + " - " + album.artist + "</a><br>"
	
	# return HttpResponse(template.render(context, request)) -- HttpResponse is inbuilt in render
	return render(request, 'music/index.html', context)

def details(request, album_id):
	# html = "<h1>This is Album no. : " + str(album_id) + "</h1>" ---> Using template now. 
	# Using exception handling to catch the invalid request.


	# There is a shortcut for try-except statement as well..Mentioned right below raise
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/details.html', { 'album': album })

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/details', {
				'album': album,
				'error_message': "Valid song not selected"
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/details.html', { 'album': album })