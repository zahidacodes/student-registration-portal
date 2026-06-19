from django.contrib import admin
from .models import myclass

# Register your models here.
@admin.register(myclass)
class myadmin(admin.ModelAdmin):
    list_display = ["name","address","branch","ph_number"]