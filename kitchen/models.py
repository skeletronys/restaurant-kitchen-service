from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes/')
    cooks = models.ManyToManyField(Cook)
