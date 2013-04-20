# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from cinema.models import Movie
from django.contrib.comments.models import Comment
from cinema.user_register import username
#from django.contrib.comments.views.comments import post_free_comment

# Вывод данных о фильмах на главную
def index(request):
    movie = Movie.objects.all()
    return render_to_response('index.html', {'movie': movie}, context_instance=RequestContext(request, processors=[username]))

# Открывает детальное описание поста
def post(request, id_movie):
    link = "http://%s/cinema/main/%s" % (request.get_host(), id_movie)
    movie = Movie.objects.filter(id__in=id_movie)
    return render_to_response('post.html', {'link': link, 'movie': movie}, context_instance=RequestContext(request, processors=[username]))

def archive(request):   
    posts = Comment.objects.all()   
    return render_to_response('comments/freeform.html', {'posts': posts}, context_instance=RequestContext(request, processors=[username]))

"""
def post_comment(request):
    if request.has_key('url') and not request.has_key('preview'):
        responce = post_free_comment(request)
        if len(request['url'].strip()) > 0 and isinstatnce(responce, HttpResponseRedirect):
            return HttpResponseRedirect(request['url'])
            return responce
        return post_free_comment(request)
"""