from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Personal
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    return render(request, 'view/index.html', )


def menu(request):
    menu_items = Menu.objects.all()
    paginator = Paginator(menu_items, 3)
    page = request.GET.get('page')

    try:
        menu_items = paginator.page(page)
    except PageNotAnInteger:
        menu_items = paginator.page(1)
    except EmptyPage:
        menu_items = paginator.page(paginator.num_pages)

    return render(request, 'view/menu.html', {"menu": menu_items})


def dish(request, slug):
    menu_item = get_object_or_404(Menu, slug=slug)
    return render(request, 'view/dish.html', {"menu_item": menu_item})


def personal(request):
    personal_prof = Personal.objects.all()

    return render(request, 'view/personal.html', {"personal": personal_prof})
