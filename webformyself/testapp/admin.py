from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Genre, Article

admin.site.register(Genre, MPTTModelAdmin)
admin.site.register(Article)