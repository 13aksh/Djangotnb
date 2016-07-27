from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album



class Index(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()


class Details(generic.DetailView):
	model = Album
	template_name = 'music/details.html'

class AddAlbum(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class UpdateAlbum(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class DeleteAlbum(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')
