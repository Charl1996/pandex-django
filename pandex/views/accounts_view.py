from django.shortcuts import render
from ..app.pantry import AppPantry as Pantry
from ..app.account import AppAccount as Account
from django.views.decorators.csrf import csrf_exempt

import json
import django.views.decorators.http as method
import django.http as http


@csrf_exempt
@method.require_POST
def new_account(request):
    body = json.loads(request.body)
    account = Account().create_new_account(body)
    return ""


@csrf_exempt
@method.require_POST
def login(request):

    return http.HttpResponse("Not implemented")
