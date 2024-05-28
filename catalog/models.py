from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Наименование категории",
    )
    category_description = models.TextField(
        verbose_name="Описание", help_text="Сделайте описание категории", **NULLABLE
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Наименование продукта"
    )
    description = models.TextField(
        verbose_name="Описание", **NULLABLE, help_text="Описание продукта"
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию",
        **NULLABLE,
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата последнего изменения"
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE
    )

    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name", "category"]


class Version(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="version",
    )

    number_version = models.IntegerField(default=1, verbose_name="номер версии")

    name_version = models.CharField(max_length=150, verbose_name="имя версии")

    version_flag = models.BooleanField(default=False, verbose_name="признак версии")

    class Meta:
        verbose_name = "версия продукта"
        verbose_name_plural = "версии продуктов"

        def __str__(self):
            return f"{self.name_version}"
