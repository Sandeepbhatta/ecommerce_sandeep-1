# Lab 2 E-Commerce

## a. Objective

Learn how to use a Foreign Key and how to put it into practice.
To understand how to utilize Relationship in an ER diagram and how to apply it properly.

## b. Introduction

1. Foreign Key
   A foreign key is a column or set of columns in a relational database table that connects data from two tables. It serves as a cross-reference between tables by referencing the primary key of another table and therefore creating a relationship between them.
2. Relationship
   In the context of databases, a relationship is a situation in which one table has a foreign key that references the primary key of the other table. Relationships enable relational databases to partition and store data in several tables while also linking disparate data pieces.

## c. Procedure

We did the following steps in this lab:

1. In the product_module module, open “models.py” and edit code for Brand model

```python
   class Brand(models.Model):
   name = models.CharField(max_length=200)
   is_active = models.BooleanField()
```

2. Similarly, edit code for Category

```python
class Category(models.Model):
name = models.CharField(max_length=200, default='')
is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = "Categories"
```

3. And at last edit code for Product model.

```python
class Product(models.Model):
name = models.CharField(max_length=200)
price = models.FloatField()
quantity = models.IntegerField()
image_url = models.CharField(max_length=500)
color_code = models.CharField(max_length=20)
brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
category = models.ForeignKey(Category, on_delete=models.CASCADE)
registered_on = models.DateTimeField()
is_active = models.BooleanField()
```

4. We will use sqllite3 which is default database in Django

```python
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}
```

5. Ensure database table for added model is created properly
   - python manage.py makemigrations
   - python manage.py migrate
6. In database tool, verify that the added table is created properly
7. Goto “admin.py” and add the following code

```python
from .models import Brand, Category, Product
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
```

8. Run the server and verify CRUD operation
   - python manage.py runserver
9. Perform: create, read, update, delete operation from admin panel

## d. observation:

Each model inherits “models.Model”.
Use of ForeignKey for one-to-many relationship.
Use of max_length in CharField.
Use of on_delete=models.CASCADE for ForeignKey.
Use of CharField, FloatField, IntegerField, DateTimeField, BooleanField, ForeignKey.

## e. Conclusion

Thus, in this lab, we learned about the use of Foreign keys, relationships in the ER-diagram using Django, and generated three tables to see how they interacted at the implementation level.
