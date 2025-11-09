from django import forms
from .models import TableBooking


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['name', 'phone', 'email', 'order_time', 'people_count']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше ФИО'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (XXX) XXX-XX-XX'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.ru'
            }),
            'order_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'people_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '6'
            }),
        }
        labels = {
            'name': 'ФИО',
            'phone': 'Телефон',
            'email': 'Email',
            'order_time': 'Время бронирования',
            'people_count': 'Количество человек',
        }
