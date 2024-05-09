from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import (
    DishType,
    Dish,
    Cook, Ingredient
)


class DishTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = (
            "name",
        )

    def clean_license_number(self):
        return self.cleaned_data["name"]


class DishTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]

    def clean_license_number(self):
        return self.cleaned_data["name"]


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


class DishCreateForm(forms.ModelForm):
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


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name dish"}
        )
    )
#Cook


class CookCreationForm(UserCreationForm):
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
#Ingredients


class IngredientCreationForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            "name",
        )


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by ingredient name"}
        ))