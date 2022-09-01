from .models import Purchase, Ingredient, MenuItem, RecipeRequirement
from django import forms

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("__all__")



