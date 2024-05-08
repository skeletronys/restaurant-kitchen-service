from django.urls import path

from kitchen.views import (
    index,
    DishTypeViewList,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishTypeViewList.as_view(), name="dish-type-list"),
    path("dishes/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]


app_name = 'kitchen'
