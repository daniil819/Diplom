from django.urls import path
from . import views

urlpatterns = [
    path('table-booking/', views.table_booking, name='table_booking'),
]
