from django import forms
from .models import Photo

class AddPhotoForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ['title', 'info', 'year', 'image', 'tags', 'serie']

		widgets = {
			'info': forms.Textarea(attrs={'id': 'info'})
		}