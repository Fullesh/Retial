from django.db import models

# Create your models here.


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    apartment = models.CharField(max_length=30, verbose_name='Номер дома')
