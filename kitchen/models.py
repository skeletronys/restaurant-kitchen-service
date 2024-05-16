from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


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
    image = models.ImageField(null=True, blank=True)
    cooks = models.ManyToManyField(Cook, related_name='cooked_dishes')

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)


@receiver(post_delete, sender=Dish)
def dish_post_delete_handler(sender, instance, **kwargs):
    for upload_file in instance.uploadfiles_set.all():
        upload_file.file.delete()


class UploadFiles(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    file = models.FileField(upload_to='dishes')
