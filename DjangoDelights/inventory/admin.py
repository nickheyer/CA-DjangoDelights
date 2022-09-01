from imp import PY_RESOURCE
from django.contrib import admin
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase


# Register your models here.
admin.site.register(
    [
        Ingredient, 
        RecipeRequirement, 
        MenuItem, 
        Purchase
    ])