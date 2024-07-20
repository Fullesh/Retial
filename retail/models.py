from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название продукта')
    product_description = models.TextField(verbose_name='Описание продукта', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}, {self.product_description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


