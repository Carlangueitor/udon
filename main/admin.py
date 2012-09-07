from django.contrib import admin
from main.models import Show, Demography, Genre, Episode

admin.site.register(Demography)
admin.site.register(Genre)
admin.site.register(Show)
admin.site.register(Episode)
