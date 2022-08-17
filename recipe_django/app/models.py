from django.db import models

class IngredientInfo(models.Model):
    name = models.CharField(max_length = 100)

class Ingredient(models.Model):
    ingredient_info = models.ForeignKey(to = IngredientInfo, on_delete=models.CASCADE)
    amount = models.CharField(max_length = 100, blank=True, default='')

class Recipe(models.Model):
    ingredient = models.ManyToManyField(to = Ingredient)
    instructions = models.TextField(blank=True, default = '')
    