from django.db import models
from django.utils.timezone import now

# Create your models here.


class Ingredient(models.Model):
    """
    This model represents an ingredient that the restaurant has in its inventory.
    """
    name = models.CharField(name="name", unique=True, max_length=100)
    quantity = models.FloatField(name="quantity", default=0) #Quantity currently available in storage
    unit_type = models.CharField(name="unittype", default="Ct", max_length=10, verbose_name="Unit Type")
    price_per = models.FloatField(name="priceper", default=0.00, verbose_name="Price Per")
    image_link = models.CharField(name="image", default="https://icon-library.com/images/ingredient-icon/ingredient-icon-6.jpg", max_length=200)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/ingredients"

class MenuItem(models.Model):
    """
    This model represents an item on the restaurants menu.
    """
    name = models.CharField(name="name", unique=True, max_length=100)
    price = models.FloatField(name="price", default=0.00)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
    
    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    """
    Represents a single ingredient and how much of it is required for an item off the menu. Ie: 2 cups of sugar for 1 cake
    """
    
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(name="amount")
    
    class Meta:
        verbose_name = "Recipe Requirement"
        verbose_name_plural = "Recipe Requirements"
    
    def __str__(self):
        return f"{self.menu_item} | {self.ingredient} | {self.amount}"

class Purchase(models.Model):
    """
    Represents a customer purchase of an item off the menu.
    """
    customer = models.CharField(default="Customer", name="customer", max_length=100)
    timestamp = models.DateTimeField(default=now, name="timestamp")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.timestamp} | {self.menu_item} | {self.customer}"