from django.shortcuts import (
	render,
	redirect,
	get_object_or_404
)

from django.views.generic import (
	ListView, 
	CreateView
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from photos.models import *
from .forms import AddPhotoForm


# ФУНКЦИИ-ПРЕДСТАВЛЕНИЯ
def index(request):
	return render(request, 'photos/index.html', context={'title': 'Главная'})

def contacts(request):
	return render(request, 'photos/contacts.html', context={'title': 'Контакты'})

# КЛАССЫ-ПРЕДСТАВЛЕНИЯ
class PhotosListView(ListView):
	paginate_by = 5
	model = Photo
	template_name = 'photos/show_photos.html'
	context_object_name = 'photos'
	extra_context = {'title': 'Все фотографии'}

	def get_queryset(self):
		return Photo.objects.all()

class SeriesListView(ListView):
	model = Serie
	template_name = 'photos/series.html'
	context_object_name = 'series'
	extra_context = {'title': 'Циклы фотографий'}

class SerieListView(ListView):
	paginate_by = 5
	model = Photo
	template_name = 'photos/show_photos.html'
	context_object_name = 'photos'

	def get_queryset(self):
		return Photo.objects.filter(serie__slug=self.kwargs['serie_slug'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = f"Фотографии цикла \"{context['photos'][0].serie}\""
		return context

class TagListView(ListView):
	paginate_by = 5
	model = Photo
	template_name = 'photos/show_photos.html'
	context_object_name = 'photos'

	def get_queryset(self):
		return Photo.objects.filter(tags__slug=self.kwargs['tag_slug'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
		context['title'] = f"Фотографии по тегу \"{tag}\""
		return context

class AddPhoto(LoginRequiredMixin, CreateView):
	form_class = AddPhotoForm
	template_name = 'photos/add_photo.html'
	success_url = reverse_lazy('photos')
	login_url = '/admin/'