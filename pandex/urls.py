from django.urls import path
from . import views

urlpatterns = [
    path('accounts/new', views.accounts_view.new_account),
    path('accounts/user/login', views.accounts_view.login),
    path('pantry/<pantry_id>/ingredients',
         views.pantries_view.get_all_pantry_ingredients),
    path('pantry/<pantry_id>/ingredients/new/',
         views.pantries_view.create_pantry_ingredient),
    path('pantry/ingredients/<pantry_ingredient_id>/',
         views.pantries_view.remove_ingredient_from_pantry),
    path('pantry/ingredients/<pantry_ingredient_id>/',
         views.pantries_view.update_ingredient_in_pantry),
]
