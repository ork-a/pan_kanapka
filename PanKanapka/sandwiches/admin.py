from django.contrib import admin
from .models import Allergen, Ingredient, Sandwich, IngredientGroup

admin.site.register(Allergen)
admin.site.register(Ingredient)
admin.site.register(Sandwich)
admin.site.register(IngredientGroup)


