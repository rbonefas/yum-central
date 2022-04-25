from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Restaurant,Employee,Location,Cost,Financial)
class ViewAdmin(admin.ModelAdmin):
    pass



