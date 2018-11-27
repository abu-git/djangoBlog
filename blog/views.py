from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
	{
		'author': 'MHP',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'November 26, 2018'
	},
	{
		'author': 'Solid',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'November 26, 2018'
	}
]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')