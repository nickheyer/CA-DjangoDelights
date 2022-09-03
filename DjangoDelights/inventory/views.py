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

    def get_context_data(self, **kwargs):

        m_items = list()
        for x in MenuItem.objects.all():
            m_item = dict()
            m_item["model"] = x
            m_item["recipe"] = list()
            for y in RecipeRequirement.objects.all():
                if y.menu_item == x:
                    m_item["recipe"].append(y)
            m_items.append(m_item)


        ctx = super(MenuList, self).get_context_data(**kwargs)
        ctx['items'] = m_items
        return ctx


class MenuCreate(CreateView, LoginRequiredMixin):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menu_create_form.html"

class MenuUpdate(UpdateView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/menu_update_form.html"
    fields = ("__all__")

class MenuDelete(DeleteView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/menu_delete_form.html"
    success_url = "/menu"





class RecipeRequirementCreate(CreateView, LoginRequiredMixin):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirement_create_form.html"

class RecipeRequirementUpdate(UpdateView, LoginRequiredMixin):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirement_update_form.html"

class RecipeRequirementDelete(DeleteView, LoginRequiredMixin):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = "/menu"



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

        purchases = list()
        for x in Purchase.objects.all():
            purchase = dict()
            purchase["model"] = x
            purchase["cost"] = 0
            for y in x.menu_item.reciperequirement_set.all():
                purchase["cost"] += y.amount*y.ingredient.priceper
            purchase["profit"] = x.menu_item.price - purchase["cost"]
            purchases.append(purchase)
        ctx = super(PurchaseList, self).get_context_data(**kwargs)
        ctx["revenue"] = self.revenue()
        ctx["cost"] = self.cost()
        ctx["profit"] = self.profit()
        ctx["purchases"] = purchases
        return ctx   

class PurchaseCreate(CreateView, LoginRequiredMixin):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_create_form.html"

class PurchaseDelete(DeleteView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = "/purchases"