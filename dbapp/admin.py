from django.contrib import admin

from .models import Author, Category, Blogpost

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Blogpost)
