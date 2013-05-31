# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User

# Регистрация пользователя
def registration(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('login', ''):
			errors.append('Введите логин')
		if not request.POST.get('email', ''):
			errors.append('Введите E-mail')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Введите корректный E-mail')
		if not request.POST.get('password', ''):
			errors.append('Введите пароль')
		if not request.POST.get('password_again', ''):
			errors.append('Повторите пароль')
		if request.POST.get('password_again') != request.POST['password']:
			errors.append('Повторите пароль корректно')
		if not errors:
			user = User.objects.create_user(username=request.POST['login'], email=request.POST['email'], password=request.POST['password'])
			user.save()
			login = auth.authenticate(username=request.POST['login'], password=request.POST['password'])
			if login is not None and login.is_active:
				auth.login(request, login)
			return HttpResponseRedirect('/cinema/main/')
	return render_to_response('registration.html', {
		'errors': errors,
		}, context_instance=RequestContext(request, processors=[username]))

# Авторизация пользователя
def login(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('username', ''):
			errors.append('Введите логин')
		if not request.POST.get('userpass', ''):
			errors.append('Введите пароль')
		if not errors:
			user = auth.authenticate(username=request.POST['username'], password=request.POST['userpass'])
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect('/cinema/main/')
			else:
				return HttpResponseRedirect('')
	return render_to_response('login.html', {'errors': errors}, context_instance=RequestContext(request, processors=[username]))

# Отображение текущего авторизованного пользователя
def username(request):
	auth_user = None
	if request.user.is_authenticated():
		auth_user = request.user.username
	return {'auth_user': auth_user}

# Выход пользователя
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/cinema/main/')