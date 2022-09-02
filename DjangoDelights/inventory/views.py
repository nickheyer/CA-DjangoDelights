from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Purchase, Ingredient, MenuItem, RecipeRequirement
from .forms import IngredientForm, PurchaseForm, RecipeRequirementForm, MenuItemForm


# Create your views here.



class Home(TemplateView):
    template_name = "inventory/index.html"

class IngredientList(ListView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class IngredientCreate(CreateView, LoginRequiredMixin):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_create_form.html"

class IngredientUpdate(UpdateView, LoginRequiredMixin):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_update_form.html"
    
class IngredientDelete(DeleteView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/ingredients"

class MenuList(ListView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/menu.html"
    fields = ("__all__")

class MenuCreate(CreateView, LoginRequiredMixin):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menu_create_form.html"

class RecipeRequirementCreate(CreateView, LoginRequiredMixin):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirement_create_form.html"

class PurchaseList(ListView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/purchases.html"
    fields = ("__all__")

    def revenue(self):
        total = 0
        for x in Purchase.objects.all(): 
            total += x.menu_item.price
        return total
    
    def cost(self):
        total = 0
        for x in Purchase.objects.all():
            for y in x.menu_item.reciperequirement_set.all():
                total += y.amount*y.ingredient.priceper
        return total
    
    def profit(self):
        return self.revenue() - self.cost()

    def get_context_data(self,*args, **kwargs):
        context = {"revenue":self.revenue(), "cost":self.cost(), "profit": self.profit()}
        return context   

class PurchaseCreate(CreateView, LoginRequiredMixin):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_create_form.html"

