from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    recipe = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Personal(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
