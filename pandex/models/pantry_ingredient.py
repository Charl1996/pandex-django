from django.db import models
from django.contrib.auth.models import Group
from .pantry import Pantry
from .ingredient import Ingredient


class PantryIngredient(models.Model):
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=200)
    pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
