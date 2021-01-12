from django.shortcuts import render
from ..app.pantry import AppPantry as Pantry
from django.views.decorators.csrf import csrf_exempt

import json
import django.views.decorators.http as method
import django.http as http
