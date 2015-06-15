from django.contrib import admin
from .models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    list_display = ('name', 'views', 'likes', 'slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url', 'views')
    list

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
