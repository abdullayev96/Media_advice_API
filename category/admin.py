from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
      list_display = ['id', 'name', 'body', 'image', 'created_at']


      search_fields = ['name']
      list_filter = ['name']


admin.site.register(Category, CategoryAdmin)