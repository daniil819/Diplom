from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    recipe = models.CharField(max_length=2000)
    ingredients = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=250, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'Меню'


class Personal(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'работника'
        verbose_name_plural = 'Персонал'
