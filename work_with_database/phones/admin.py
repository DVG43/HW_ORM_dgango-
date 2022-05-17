from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_filter = ['name', 'image', 'prise', 'release_date', 'lte_exists', ]
    #prepopulated_fields = {'slug': ('name',)}
    pass


# Register your models here.
#id;name;image;price;release_date;lte_exists