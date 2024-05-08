from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = 'cook'
        verbose_name_plural = 'cooks'


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredient_dishes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='type_dishes')
    image = models.ImageField(upload_to='dishes/')
    cooks = models.ManyToManyField(Cook, related_name='cooked_dishes')
