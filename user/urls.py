from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from user import views
from django.conf import settings

urlpatterns = [
    path('signup/', views.signup_user, name="signup"),

]
