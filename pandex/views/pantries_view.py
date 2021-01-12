from django.shortcuts import render
from ..app.pantry import AppPantry as Pantry
from django.views.decorators.csrf import csrf_exempt

import json
import django.views.decorators.http as method
import django.http as http


@csrf_exempt
@method.require_GET
def get_all_pantry_ingredients(request, pantry_id):
    ingredients = Pantry.list_all_ingredients(pantry_id)

    return http.HttpResponse("Not implemented")


@csrf_exempt
@method.require_POST
def create_pantry_ingredient(request, pantry_id):
    attrs = json.loads(request.body)
    ingredient = Pantry.add_new_pantry_ingredient(pantry_id, attrs)

    return http.HttpResponse("Not implemented")


@csrf_exempt
@method.require_http_methods(["PUT"])
def update_ingredient_in_pantry(request, pantry_ingredient_id):
    attrs = json.loads(request.body)
    Pantry.update_ingredient_in_pantry(pantry_ingredient_id, attrs)
    return http.HttpResponse("")


@csrf_exempt
@method.require_http_methods(["DELETE"])
def remove_ingredient_from_pantry(request, pantry_ingredient_id):
    Pantry.remove_ingredient_from_pantry(pantry_ingredient_id)
    return http.HttpResponse("")
