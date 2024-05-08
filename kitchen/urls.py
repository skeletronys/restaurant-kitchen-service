from django.urls import path

from kitchen.views import (
    index,
    DishTypeViewList,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishViewList,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes-type/", DishTypeViewList.as_view(), name="dish-type-list"),
    path("dishes-type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes-type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishViewList.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]


app_name = 'kitchen'
