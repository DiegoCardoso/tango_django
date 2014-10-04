from django.db import models

class Category(models.Model):
	"""docstring for Category"""
	
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	def __str__(self):
		return self.name


class Page(models.Model):
	"""docstring for Page"""
	
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.title
		
