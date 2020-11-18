from django.contrib import admin

# Register your models here.

from .models import Item, Shop, Keyword, FlowerColor, FlowerType

admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Keyword)
admin.site.register(FlowerColor)
admin.site.register(FlowerType)
