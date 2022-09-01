from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("ingredients/<int:pk>/delete", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("ingredients/", views.IngredientList.as_view(), name="ingredients"),
    path("menu/", views.MenuList.as_view(), name="menu"),
    path("purchases/", views.PurchaseList.as_view(), name="purchases"),
    
]
