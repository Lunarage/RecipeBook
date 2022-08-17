from django.contrib import admin

from .models import IngredientInfo, Ingredient, Recipe

admin.site.register(IngredientInfo)
admin.site.register(Ingredient)
admin.site.register(Recipe)