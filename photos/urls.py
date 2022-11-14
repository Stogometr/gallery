from django.urls import path

from .views import *


urlpatterns = [
# 	path('путь', функция в файле views, имя)

	path('', index, name='home'),
	path('photos/', PhotosListView.as_view(), name='photos'),
	path('add_photo/', AddPhoto.as_view(), name='add_photo'),
	path('contacts/', contacts, name='contacts'),
	path('series/', SeriesListView.as_view(), name='series'),
	path('serie/<slug:serie_slug>/', SerieListView.as_view(), name='serie'),
	path('tag/<slug:tag_slug>', TagListView.as_view(), name='tag'),
]