from django import forms

from kitchen.models import DishType


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


