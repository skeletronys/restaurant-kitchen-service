from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import DishType, Dish, Cook
from kitchen.templatetags.forms import (
    DishTypeSearchForm,
    DishSearchForm
)


def index(request):
    """View function for the home page of the site."""

    num_dish_type = DishType.objects.count()
    num_dish = Dish.objects.count()
    num_cook = Cook.objects.count()

    context = {
        "num_dish_type": num_dish_type,
        "num_dish": num_dish,
        "num_cook": num_cook,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeViewList(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/DishType/DishType_list.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeViewList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        username = self.request.GET.get("name")

        if username:
            return self.model.objects.filter(name__icontains=username)

        return self.model.objects.all()


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/DishType/DishType_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/DishType/DishType_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "kitchen/DishType/DishType_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")
#DishView


class DishViewList(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/Dish/Dish_list.html"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishViewList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        username = self.request.GET.get("name")

        if username:
            return self.model.objects.filter(name__icontains=username)

        return self.model.objects.all()


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/Dish/Dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/Dish/Dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "kitchen/Dish/Dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")
