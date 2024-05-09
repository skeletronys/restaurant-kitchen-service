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
    CookViewList,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    IngredientsViewList,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
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
    path("cook/", CookViewList.as_view(), name="cook-list"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("ingredients/", IngredientsViewList.as_view(), name="ingredients-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredients-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredients-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredients-delete"),
]


app_name = 'kitchen'
