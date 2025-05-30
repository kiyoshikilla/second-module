from django.contrib import admin
from .models import Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    fields = (
        'title',
        'category',
        'description',
        'ingredients',
        'instructions',
        'created_at',
        'updated_at',
    )
    # readonly_fields = ('created_at', 'updated_at')  # Не потрібне, якщо хочете редагувати дати

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)