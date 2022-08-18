from django.test import TestCase
from recipe_django.app.models import IngredientInfo

class SignalsTestCase(TestCase):
    def setup(self):
        IngredientInfo.objects.create(name='apple')