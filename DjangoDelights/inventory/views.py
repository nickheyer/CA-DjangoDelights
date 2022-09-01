from ast import In
from distutils.log import Log
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Purchase, Ingredient, MenuItem, RecipeRequirement
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.



class Home(TemplateView):
    template_name = "inventory/index.html"

class IngredientList(ListView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class IngredientDelete(DeleteView, LoginRequiredMixin):
    model = Ingredient
    success_url = "ingredients"

class MenuList(ListView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/menu.html"

class PurchaseList(ListView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/purchases.html"

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

