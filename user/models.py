from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name