from .models import Brand, Category, Product
from django.contrib import admin

# Register your models here.

# from .models import Brand

# admin.site.register(Brand)
from .models import Brand
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
