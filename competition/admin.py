from django.contrib import admin
from .models import Competition, Entry, Winner

admin.site.register(Competition)
admin.site.register(Entry)
admin.site.register(Winner)
