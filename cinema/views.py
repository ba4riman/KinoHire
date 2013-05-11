# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from cinema.models import Movie
from django.contrib.comments.models import Comment
from cinema.user_register import username
from django.db.models import Q

# Вывод данных о фильмах на главную
def index(request):
	movie = Movie.objects.all()
	return render_to_response('index.html', {'movie': movie}, context_instance=RequestContext(request, processors=[username]))

# Открывает детальное описание поста
def post(request, id_movie):
	movie = Movie.objects.filter(id__in=id_movie)
	return render_to_response('post.html', {'movie': movie}, context_instance=RequestContext(request, processors=[username]))

# Поиск фильмов по параметрам: название, жанр, страна, актер, режиссер
def search(request):
	error = False
	if 'search' in request.GET:
		search = request.GET['search']
		if not search:
			error = 'Введите параметр запроса'
		else:
			result_movie = Movie.objects.filter(Q(title__icontains=search) |
				Q(country__name__icontains=search) |
				Q(genre__name__icontains=search) |
				Q(director__first_name__icontains=search) |
				Q(director__last_name__icontains=search) |
				Q(actor__first_name__icontains=search) |
				Q(actor__last_name__icontains=search))
			return render_to_response('search.html', {
				'result_movie': result_movie,
				'search': search
				})
	return render_to_response('search.html', {'error': error}, context_instance=RequestContext(request, processors=[username]))

def add_comment(request):
	pass