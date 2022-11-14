from django.contrib import admin

from .models import *

class PhotoAdmin(admin.ModelAdmin): #Настраивает отображение модели в админке
	list_display = ('id', 'image', 'year') #Какие поля будут отображаться
	list_display_links = ('id', 'year') #На какие поля можно кликнуть, чтобы перейти к редактированию записи
	search_fields = ('title', 'info', 'year') #По каким полям можно искать записи

class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'tag_name', 'slug')
	list_display_links = ('id', 'tag_name')
	search_fields = ('tag_name',) #Принимает кортеж, поэтому обязательно должна стоять запятая, если в кортеже 1 элемент

class SerieAdmin(admin.ModelAdmin):
	list_display = ('id', 'ser_name', 'slug')
	list_display_links = ('id', 'ser_name')
	search_fields = ('ser_name',) #Принимает кортеж, поэтому обязательно должна стоять запятая, если в кортеже 1 элемент

# Register your models here.
admin.site.register(Photo, PhotoAdmin) #Вторым параметром указывается класс, в котором настраивается отображение
admin.site.register(Tag, TagAdmin)
admin.site.register(Serie, SerieAdmin)