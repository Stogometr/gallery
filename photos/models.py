from django.db import models
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
	title = models.CharField(max_length=256, blank=True, verbose_name='Название фотографии')
	info = models.TextField(blank=True, verbose_name='Информация о фотографии')
	year = models.CharField(max_length=4, verbose_name='Год')
	image = models.ImageField(upload_to='photos/', verbose_name='Файл')
	tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
	serie = models.ForeignKey('Serie', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Цикл')

	def get_tags(self):
		return self.tags.all()

	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'
		ordering = ['-id']

class Tag(models.Model):
	tag_name = models.CharField(max_length=100, db_index=True, verbose_name='Тег')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	
	def __str__(self):
		return self.tag_name

	def get_slug(self):
		return reverse('tag', kwargs={'tag_slug': self.slug})

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'
		ordering = ['id']

class Serie(models.Model):
	ser_name = models.CharField(max_length=100, verbose_name='Цикл')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
	
	def __str__(self):
		return self.ser_name

	def get_url(self):
		return reverse('serie', kwargs={'serie_id': self.id})

	def get_slug(self):
		return reverse('serie', kwargs={'serie_slug': self.slug})

	class Meta:
		verbose_name = 'Цикл фотографий'
		verbose_name_plural = 'Циклы фотографий'
		ordering = ['id']