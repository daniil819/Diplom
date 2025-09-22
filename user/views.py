from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
import re


def signup_user(request):
    if request.method == "GET":
        return render(request, 'user/singupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'user/signup.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует. Задайте другое'})
        else:
            return render(request, 'user/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('index')


def login_user(request):
    if request.method == "GET":
        return render(request, 'user/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа',
                'username': request.POST['username']
            })
        else:
            login(request, user)
            return redirect('index')



