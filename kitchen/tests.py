from django.test import TestCase
from django.urls import reverse

from .forms import DishForm
from .models import Cook, Dish, DishType, Ingredient


class CookModelTest(TestCase):
    def test_cook_str(self):
        cook = Cook.objects.create_user(username='testuser', password='testpass', years_of_experience=1)
        self.assertEqual(str(cook), cook.username)


class DishModelTest(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        dish = Dish.objects.create(name='Test Dish', price=10.99, dish_type=dish_type)
        self.assertEqual(str(dish), "Test Dish")


class DishTypeModelTest(TestCase):
    def test_name_label(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        field_label = dish_type._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        max_length = dish_type._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class IngredientModelTest(TestCase):
    def test_name_label(self):
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class DishFormTest(TestCase):
    def test_form_no_data(self):
        form_data = {}
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_form_valid_data(self):
        dish_type = DishType.objects.create(name='Test Dish Type')
        cook = Cook.objects.create_user(username='testuser', password='testpass', years_of_experience=1)
        ingredient = Ingredient.objects.create(name='Test Ingredient')

        form_data = {
            'name': 'Test Dish',
            'price': 10.99,
            'description': "test description",
            'dish_type': dish_type.pk,
            'cooks': [cook.pk],
            'ingredients': [ingredient.pk],
        }

        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())


class DishTypeListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('kitchen:dish-type-list'))
        self.assertEqual(response.status_code, 200)


class IngredientListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('kitchen:ingredients-list'))
        self.assertEqual(response.status_code, 302)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('kitchen:ingredients-list'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login/'))

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('kitchen:ingredients-list'))
        self.assertEqual(response.status_code, 302)


class CookListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('kitchen:cook-list'))
        self.assertEqual(response.status_code, 200)


class DishTypeCreateViewTest(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(username='testuser', password='testpass', years_of_experience=1)

    def test_can_create_dish_type(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('kitchen:dish-type-create'), {'name': 'Test Dish Type'})
        self.assertEqual(response.status_code, 302)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('kitchen:dish-type-create'))
        self.assertEqual(response.status_code, 302)
