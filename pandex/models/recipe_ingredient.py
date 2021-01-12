from django.db import models
from django.contrib.auth.models import Group
from .recipe import Recipe
from .ingredient import Ingredient


class RecipeIngredient(models.Model):
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return '%d%s %s' % (self.quantity, self.unit, self.ingredient.name)
