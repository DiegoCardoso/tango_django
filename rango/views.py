from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category, Page
from rango.help import encode_category_name, decode_category_name

def index(request):
	#Request the context of the request
	#The context contains information such as the client's machine details, for example.
	context = RequestContext(request)

	#Construct a dictionary to pass to the template engine as its context.
	#Note the key boldmessage is the same as {{ boldmessage}} in the template!
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = { 'categories': category_list }

	for category in category_list:
		category.url = encode_category_name(name=category.name)

	page_list = Page.objects.order_by('-views')[:5]
	context_dict['pages'] = page_list

	#Return a rendered responseto send to the client
	#We make use of the shortcut function to make out lives easier.
	#Note that the first parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)

	return render_to_response('rango/about.html', {}, context)

def category(request, category_name_url):
	context = RequestContext(request)

	category_name = decode_category_name(name=category_name_url)

	context_dict = {'category_name': category_name}

	try:
		
		category = Category.objects.get(name=category_name)

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	
	return render_to_response('rango/category.html', context_dict, context)