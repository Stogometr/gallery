from django import template
from photos.models import *
from photos.views import (
	PhotosListView,
	SerieListView,
	TagListView,
)

register = template.Library()

@register.inclusion_tag('photos/inclusion_tags/header_menu.html')
def header_menu():
	header_menu = [
		{'title': 'На главную', 'url_name': 'home'},
		{'title': 'Все фотографии', 'url_name': 'photos'},
		{'title': 'Контакты', 'url_name': 'contacts'},
		{'title': 'Циклы фотографий', 'url_name': 'series'}
	]

	return {'menu': header_menu}

@register.inclusion_tag('photos/inclusion_tags/pagination.html', takes_context=True)
def pagination(context):
	paginator = context['paginator']
	page_obj = context['page_obj']

	return {'paginator': paginator, 'page_obj': page_obj}

@register.inclusion_tag('photos/inclusion_tags/show_photos.html', takes_context=True)
def show_photos(context):
	photos = context['photos']

	return {'photos': photos}

@register.simple_tag()
def get_tags(photo):
	return photo.tags.all()