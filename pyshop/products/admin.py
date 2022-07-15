from django.contrib import admin
from .models import Products, Offer



class Productadmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class Offeradmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Register your models here.
admin.site.register(Products, Productadmin)
admin.site.register(Offer, Offeradmin)
