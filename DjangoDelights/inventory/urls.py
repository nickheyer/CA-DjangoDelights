from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("logout/", views.logout_user, name="logout"),

    path("ingredients/", views.IngredientList.as_view(), name="ingredients"),
    path("ingredients/create", views.IngredientCreate.as_view(), name="ingredient_create"),
    path("ingredients/<int:pk>/update", views.IngredientUpdate.as_view(), name="ingredient_update"),
    path("ingredients/<int:pk>/delete", views.IngredientDelete.as_view(), name="ingredient_delete"),
    
    path("menu/", views.MenuList.as_view(), name="menu"),
    path("menu/create", views.MenuCreate.as_view(), name="menu_create"),
    path("menu/<int:pk>/update", views.MenuUpdate.as_view(), name="menu_update"),
    path("menu/<int:pk>/delete", views.MenuDelete.as_view(), name="menu_delete"),

    path("requirement/create", views.RecipeRequirementCreate.as_view(), name="requirement_create"),
    path("requirement/<int:pk>/update", views.RecipeRequirementUpdate.as_view(), name="requirement_update"),
    path("requirement/<int:pk>/delete", views.RecipeRequirementDelete.as_view(), name="requirement_delete"),


    path("purchases/", views.PurchaseList.as_view(), name="purchases"),
    path("purchases/create", views.PurchaseCreate.as_view(), name="purchase_create"),
    path("purchase/<int:pk>/delete", views.PurchaseDelete.as_view(), name="purchase_delete"),
]
