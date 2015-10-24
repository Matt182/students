# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.template import RequestContext


def login(request):
    """
    Представление для входа
    """
    if auth.get_user(request).username:
        return redirect('groups/')
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('groups/')
            else:
                context = RequestContext(request, {
                    'error': 'Неверное имя или пароль!',
                })
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html')


def logout(request):
    """
    Представление для выхода из системы
    """
    auth.logout(request)
    return redirect('/')


def register(request):
    """
    Представление для регистрации новыйх пользователей
    """
    context = RequestContext(request, {
        'form': UserCreationForm(),
    })
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('../groups/')
        else:
            context['form'] = newuser_form
    return render(request, 'register.html', context)

