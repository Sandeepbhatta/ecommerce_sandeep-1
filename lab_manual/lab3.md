## Lab 3 : Search Products (Admin)

## Objective 

- To insert search feature in the product model by the admin.

## Introduction

In lab 2, we contrusted the Product category to list the products available. In this lab we will create a "Search Bar" to check whether the product is available or not. 

## Procedure 

- **In admin.py , replacing the code for product.**

```
class ProductAdmin(admin.ModelAdmin):
list_display = ["name", "price", "brand", "category",]
search_fields = ["name", "price", "brand__name", "category__name",]
list_filter = ["brand","category",]
readonly_fields = ["quantity",]
class Meta:
model = Product
admin.site.register(Product, ProductAdmin)
```

- **In admin.py , replacing the code for brand .**

```
class BrandAdmin(admin.ModelAdmin):
    list_display =["name", "is_active",]
    search_fields= ["name" ,"is_active",]
    list_filter= ["name", "is_active",]
    
    class Meta:
        model = Brand
admin.site.register(Brand, BrandAdmin)
```
-**In admin.py , replacing the code for category.**

```
class CategoryAdmin(admin.ModelAdmin):
    list_display =["name", "is_active",]
    search_fields= ["name", "is_active",]
    list_filter= ["name", "is_active",]
    
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)
```
- **In model.py , add the image_tag to the Product class.**

```
def image_tag(self):
return mark_safe(f'<img src="{self.image_url}" width="50"

height="50" />')
image_tag.short_description = "Product"
def __str__(self):
return self.name
```

- **Displaying the image of Product class in admin.py.**

```
class ProductAdmin(admin.ModelAdmin):
list_display = ["image_tag", "name", "price", "brand", "category",]
search_fields = ["name", "price", "brand__name", "category__name",]
list_filter = ["brand","category","price",]
# readonly_fields = ["quantity",]
class Meta:
model = Product
admin.site.register(Product, ProductAdmin)
```
- **Last but not least, running the project and conducting CRUD operations on Brand, Category, and Product.**

```
 python manage.py runserver
```

## Output
- **The Brand model.**
![](/lab_manual/images/b21.PNG)

- **The Category model.**
![](/lab_manual/images/c21.PNG)

- **The Product model.**
![](/lab_manual/images/p21.PNG)

## Conclusion
As a result, in this lab, we used multiple scripts to develop a search bar for items, brands, and categories, as well as display photos for products on the e-commerce site.
