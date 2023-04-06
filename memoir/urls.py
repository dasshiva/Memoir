from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name = "index"),
  path("<str:subject>/<int:formula_id>/", views.formula, name="get_formula"),
  path("<str:subject>/", views.show_all_formulae, name="show_all")
]