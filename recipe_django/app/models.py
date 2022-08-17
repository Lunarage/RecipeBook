from django.db import models

class IngredientNutr(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

class IngredientInfo(models.Model):
    name = models.CharField(max_length=255)
    ingredient_nutr = models.ManyToManyField(IngredientNutr, blank=True, null=True)

class Ingredient(models.Model):
    ingredient_info = models.ForeignKey(to= IngredientInfo, on_delete=models.CASCADE)
    amount = models.CharField(max_length=255, blank=True, default='')

class Recipe(models.Model):
    ingredient = models.ManyToManyField(to=Ingredient)
    instructions = models.TextField(blank=True, default='')