from ..models import Ingredient, PantryIngredient


class AppPantry():

    # Test
    def list_all_ingredients(pantry_id):
        return PantryIngredient.objects.filter(pantry_id=pantry_id)

    # Test
    def add_new_pantry_ingredient(pantry_id, attrs):
        ingredient_name = attrs["name"]

        ingredient = Ingredient.objects.get_or_create(name=ingredient_name)
        new_pantry_ingredient = create_pantry_ingredient(
            pantry_id,
            ingredient.id,
            attrs
        )
        return new_pantry_ingredient

    # Test
    def remove_ingredient_from_pantry(pantry_ingredient_id):
        return PantryIngredient.objects.get(id=pantry_ingredient_id).delete()

    # Test
    def update_ingredient_in_pantry(pantry_ingredient_id, attrs):
        pantry_ingredient = PantryIngredient.objects.get(pantry_ingredient_id)
        for key, value in attrs.items():
            pantry_ingredient[key] = value
        return pantry_ingredient.save()

    # Private

    def __find_pantry_ingredient(pantry_id, ingredient_name):
        pantry_ingredient = PantryIngredient.objects.get_or_create(pantry)
        return pantry_ingredient

    def __create_pantry_ingredient(pantry_id, ingredient_id, ingredient_attrs):
        pantry_ingredient = PantryIngredient(
            quantity=ingredient_attrs["quantity"],
            unit=ingredient_attrs["unit"],
            pantry_id=pantry_id,
            ingredient_id=ingredient_id
        )
