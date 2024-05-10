from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import (
    DishType,
    Dish,
    Cook,
    Ingredient,
    UploadFiles
)
from kitchen.forms import (
    DishTypeSearchForm,
    DishSearchForm,
    CookSearchForm,
    IngredientSearchForm,
    CookCreationForm
)


def index(request):
    """View function for the home page of the site."""

    num_dish_type = DishType.objects.count()
    num_dish = Dish.objects.count()
    num_cook = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_dish_type": num_dish_type,
        "num_dish": num_dish,
        "num_cook": num_cook,
        "num_ingredients": num_ingredients,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeViewList(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/DishType/DishType_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeViewList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.model.objects.filter(name__icontains=name)

        return self.model.objects.all()


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/DishType/DishType_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/DishType/DishType_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/DishType/DishType_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")
#DishView


class DishViewList(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/Dish/Dish_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishViewList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.model.objects.filter(name__icontains=name)

        return self.model.objects.all()


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/Dish/Dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/Dish/Dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/Dish/Dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/Dish/Dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")
#Cook


class CookViewList(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "kitchen/Cook/Cook_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookViewList, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")

        context["search_form"] = CookSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        last_name = self.request.GET.get("last_name")
        if last_name:
            return self.model.objects.filter(last_name__icontains=last_name)

        return self.model.objects.all()


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "kitchen/Cook/Cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/Cook/Cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/Cook/Cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen/Cook/Cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")
#Ingridients


class IngredientsViewList(generic.ListView):
    model = Ingredient
    context_object_name = "ingredients_list"
    template_name = "kitchen/Ingredients/Ingredients_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientsViewList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = IngredientSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.model.objects.filter(name__icontains=name)

        return self.model.objects.all()


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "kitchen/Ingredients/Ingredients_form.html"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    template_name = "kitchen/Ingredients/Ingredients_form.html"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = "kitchen/Ingredients/Ingredients_confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredients-list")
