# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.

from django.contrib import admin
from blog.models import Author, Article, Category,SubCategory


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'id', 'author', 'category','subcategory','publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category','create_time')
    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','create_time')
    ordering = ('create_time',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
