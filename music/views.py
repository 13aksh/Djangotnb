from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm



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

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			user = form.save(commit=False)

			#cleaned formatted data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)

			user.save()

			#returns user objects User always returns if=0 the order hai

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')


		return render(request, self.template_name, {'form': form})