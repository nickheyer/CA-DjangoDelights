from .models import Purchase, Ingredient, MenuItem, RecipeRequirement
from django import forms

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("__all__")

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ("__all__")

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("__all__")

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ("__all__")