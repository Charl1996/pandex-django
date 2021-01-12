from ..models import Recipe, RecipeIngredient


class AppRecipe():

    def list_all_recipies():
        return Recipe.objects.all()

    def add_new_recipe():
        return ""

    def update_recipe(recipe_id):
        return ""
