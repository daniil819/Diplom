from django.db import models


class TableBooking(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    order_time = models.DateTimeField(verbose_name='Время бронирования')
    people_count = models.PositiveIntegerField(verbose_name='Количество человек')

    class Meta:
        verbose_name = 'Бронирование столика'
        verbose_name_plural = 'Бронирования столиков'

    def __str__(self):
        return self.name
