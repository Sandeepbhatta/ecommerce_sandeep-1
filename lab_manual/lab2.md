## Lab 2 : Adding Brand, Category and Product

## Objective
- To include models for products, brands, and categories.
- To learn more about how to add models and how models.py works 
- To learn more about the admin.py, models.py, and other files provided by the Django framework 
- To execute CRUD operations on all three models

## Introduction
We constructed a product module in our first lab. Then we'll add a brand, a product, and a category to the product module, which also has the er model structure shown below:
![Er diagram, the product module](/lab_manual/images/er.PNG)

## Procedure 
- **In the models.py file, add the model Brand.**

```
  class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
```
- **In the models.py file, add the model Category.**

```
  class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
  class Meta:
    verbose_name_plural = "Categories"
```
- **In the models.py , add the model Product.**

```
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
- **Migrations are used to make changes to the database.**

```
  python manage.py makemigrations
  python manage.py migrate
```
- **To enable CRUD activities in the admin site, add the following code to admin.py.**

```
  from .models import Brand, Category, Product
  admin.site.register(Brand)
  admin.site.register(Category)
  admin.site.register(Product)
```

- **Last but not least, running the project and conducting CRUD operations on Brand, Category, and Product.**

```
 python manage.py runserver
```

## Output
- **Adding the models Brand, Category and Product**


![](/lab_manual/images/p1.PNG)

- **The Brand model**
![](/lab_manual/images/b1.PNG)
![](/lab_manual/images/b2.PNG)


- **The Category model**
![](/lab_manual/images/c1.PNG)

-**The Product model**
![](/lab_manual/images/pro1.PNG)
![](/lab_manual/images/pro2.PNG)

## Conclusion
As a result, we constructed the Brand, Category, and Product models for our ecommerce site in our third lab. Models are inherited by all three models. Model. The product and brand, as well as the category model, are linked by a one-to-many relationship. We've also made use of django's many data kinds.
