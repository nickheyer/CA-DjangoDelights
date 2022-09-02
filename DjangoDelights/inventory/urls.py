from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("ingredients/create", views.IngredientCreate.as_view(), name="ingredient_create"),
    path("ingredients/", views.IngredientList.as_view(), name="ingredients"),
    path("ingredients/<int:pk>/update", views.IngredientUpdate.as_view(), name="ingredient_update"),
    path("ingredients/<int:pk>/delete", views.IngredientDelete.as_view(), name="ingredient_delete"),
    
    path("menu/", views.MenuList.as_view(), name="menu"),
    path("purchases/", views.PurchaseList.as_view(), name="purchases"),
    
]
