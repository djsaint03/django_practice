from django.contrib import admin

# Register your models here.
from .models import Pet
from .models import Humans


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name","breed", "sex" ]


@admin.register(Humans)
class HumansAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "address"]