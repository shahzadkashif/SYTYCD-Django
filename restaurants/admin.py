from django.contrib import admin
from .models import Restaurant,Item #whole line was missing

admin.site.register(Restaurant)
admin.site.register(Item)
