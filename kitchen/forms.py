from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple

from kitchen.models import (
    DishType,
    Dish,
    Cook,
    Ingredient,
)


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = (
            "name",
        )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )
#Dish Forms


class DishForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Dish
        fields = (
            "name",
            "price",
            "description",
            "ingredients",
            "dish_type",
            "image",
            "cooks",
        )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name dish"}
        )
    )


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "years_of_experience"]


class CookSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by last name"}
        ))


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            "name",
        )


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by ingredient name"}
        ))
