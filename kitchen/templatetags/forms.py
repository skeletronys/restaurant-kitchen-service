from django import forms

from kitchen.models import DishType, Dish


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

    def clean_license_number(self):
        return self.cleaned_data["name", "price"]


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name"]

    def clean_license_number(self):
        return self.cleaned_data["name"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name dish"}
        )
    )
