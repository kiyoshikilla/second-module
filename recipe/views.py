# views.py
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from datetime import datetime


def main(request):
    """Відображає всі рецепти, створені у 2023 році"""
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes})


def recipe_detail(request, id):
    """Відображає детальну інформацію про конкретний рецепт"""
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})