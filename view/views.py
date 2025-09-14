from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Personal


def index(request):
    return render(request, 'view/index.html', )


def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'view/menu.html', {"menu": menu_items})


def personal(request):
    personal_prof = Personal.objects.all()
    return render(request, 'view/personal.html', {"personal": personal_prof})
