from django.db.models.signals import  post_save
from django.dispatch import receiver
from .models import IngredientInfo
import requests
import logging
import json

nutrient_keys = ['Protein', 'Carbohydrate, by difference', 'Total lipid (fat)', 'Energy']
nutrient_display_names = ['Protein', 'Carbohydrate', 'Fat', 'Energy']

@receiver(post_save, sender=IngredientInfo)
def callback_nutr(sender, instance, created, **kwargs):
    if created:
        nutr_data = call_api(instance)
        
        
def call_api(instance):
    with open("recipe_django/app/api_key.txt") as f:
            api_key = f.read()


    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    url = f"{base_url}?query={instance.name}&api_key={api_key}"
    response = requests.get(url)
    
    nutr_data = None
    if response.status_code == 200:
        nutr_data = response.json()
        with open("recipe_django/app/logs/debug.json", "w", encoding='utf-8') as g:
            json.dump(nutr_data, g, ensure_ascii=False, indent=4)
    
    return nutr_data
        
    