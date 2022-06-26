# Lab 3 Search Product(admin)

## a. Objective

1.  In the admin panel, execute search and filter operations.
2.  To comprehend FK's basic operation in an ER diagram.

## b. Introduction

1. Foreign Key
   A foreign key is a column or set of columns in a relational database table that connects data from two tables. It serves as a cross-reference between tables by referencing the primary key of another table and therefore creating a relationship between them.
2. Search in Django
   On the admin change list page, it adds a search field. When someone submits a search query in that text box, this should be set to a list of field names that will be searched.

   These fields should be text fields of some sort, such CharField or TextField.

3. Mark Safe
   It assists in establishing the text's credibility (i.e. not coming from userinput).
   Mark safe can be used to display strings in HTML that are safe to display without further escaping.

4. Meta
   Meta should be used in Django to pass information into the \_meta Options object creation process. Django's Model class takes care of having a class named Meta as an attribute.
5. Read-only fields
   It's set up in such a way that Django will read from your database fields but never try to write to them. If our fields are populated by triggers or something, that could be useful.

## c. Procedure

We did the following steps in this lab:

1. For implementation of search and other enchancement in admin panel we will go to "admin.py".Then,

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
