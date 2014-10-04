from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
	name 	= forms.CharField(max_length=128, help_text='Please, enter the category name.')
	views 	= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes	= forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	#An inline class to provide addittional information on the form
	class Meta:
		model = Category


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text='Please, enter the title of the page.')	
	url = forms.URLField(max_length=200, help_text='Please, enter the URL of the page.')
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Page

		fields = ('title', 'url', 'views')
			