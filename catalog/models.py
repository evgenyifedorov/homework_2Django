from django.db import models
from django.utils import timezone

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории',
                                     help_text='Наименование категории')
    category_description = models.TextField(verbose_name='Описание', help_text='Сделайте описание категории',
                                            **NULLABLE)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Наименование продукта')
    description = models.TextField(verbose_name='Описание', **NULLABLE, help_text='Описание продукта')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', help_text='Загрузите изображение',
                              **NULLABLE, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 help_text='Введите категорию', **NULLABLE, related_name='producns', )
    price = models.FloatField(verbose_name='Цена за покупку', )
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')

    #manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name', 'category']
