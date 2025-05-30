from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category
from datetime import datetime

class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Desserts')
        cls.recipe_2023 = Recipe.objects.create(
            title='Chocolate Cake',
            description='Decadent dessert',
            instructions='Mix and bake',
            ingredients='Chocolate, flour, eggs',
            category=cls.category,
            created_at=datetime(2023, 1, 15),
            updated_at=datetime(2023, 1, 15),
        )
        cls.recipe_2022 = Recipe.objects.create(
            title='Old Recipe',
            description='Old',
            instructions='Old',
            ingredients='Old',
            category=cls.category,
            created_at=datetime(2022, 1, 1),
            updated_at=datetime(2022, 1, 1),
        )

    def test_main_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_main_view_shows_only_2023_recipes(self):
        response = self.client.get(reverse('main'))
        recipes = response.context['recipes']
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].title, 'Chocolate Cake')

    def test_recipe_detail_view(self):
        url = reverse('recipe_detail', args=[self.recipe_2023.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Cake')

    def test_recipe_detail_404(self):
        url = reverse('recipe_detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)