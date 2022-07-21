# **Lab 4 : To add bootstrap template and adding base files**




## **Introduction**

I'll be including a bootstrap template to display our products and provide add-to-cart options.
The e-commerce website is called fruitka , and it helps you locate the best price for your fruits you need.


## **Objectives**

* Implement a bootstrap model in the django
* Connect the backend of Django with Bootstrap and perform search operation

## **Procedure**

- **Adding base template**

```
  <!DOCTYPE html>
<html lang="en">
<head>
 <link rel="stylesheet"
href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.c
ss"/>
 <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
 <script
src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
></script>
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/fontawesome/4.7.0/css/font-awesome.min.css" />
 <title>{% block title %} Electronics Commerce {% endblock %}</title>
 <style type="text/css">
 .min-h-100 { min-height: 100%; }
 </style>
</head>
<body>
 <div class="row">
 <div id="header" class="bg-info col-sm-12 col-md-12 col-lg-12">
 <div class="row">
 <div class="col-sm-4 col-md-4 col-lg-4">
 <img src="https://img.favpng.com/23/7/24/logo-e-commercedigital-marketing-brand-trade-png-favpng-xTcxcPuHCYQBUh9P8q30ETQji.jpg"
alt="E-commerce Logo" style="height:50px; width:auto;" />
 </div>
 <div class="col-sm-7 col-md-7 col-lg-7">
 <h2>
 {% block header %} Electronic Commerce {% endblock %}
 </h2>
 </div>
 <div class="col-sm-1 col-md-1 col-lg-1">
 <a class="btn btn-success btn-sm ml-3" href="#cart-model"
data-toggle="modal">
 <span>Cart</span>
 <span class="badge badge-light">
 <label id="cart_qty">0</label>
 </span>
 </a>
 </div>
 </div>
 </div>
 </div>
 <div class="row">
Electronic Commerce (Programming)
11
 <div id="sidebar" class="min-h-100 min-h-800 bg-light border col-sm-3
col-md-3 col-lg-3">
 {% block sidebar %}
 <ul>
 <li><a href="/admin/"><i class="fa fa-user" ariahidden="true"></i> Admin</a></li>
 <li><a href="/"><i class="fa fa-search" aria-hidden="true"></i>
Product</a></li>
 <li><a href="/cart/"><i class="fa fa-shopping-cart" ariahidden="true"></i> Cart</a></li>
 </ul>
 {% endblock %}
 </div>
 <div id="content" class="min-h-100 bg-light col-sm-9 col-md-9 col-lg-9">
 {% block content %}{% endblock %}
 </div>
 </div>
</body>
</html>
```
- **Ensuring base.html is globally available**

```
  ...
TEMPLATES = [
 {
 'BACKEND': 'django.template.backends.django.DjangoTemplates',
 'DIRS': [BASE_DIR / 'templates'],
...
```
- **Creating tempaltes folder inside product_module and creating index.html**

```
  {% extends "base.html" %}
{% block title %} Search {% endblock %}
{% block header %} Search Product {% endblock %}
{% block content %}
 <!--Navbar-->
 <nav class="navbar navbar-expand-lg">
 <div>
 <!-- Links -->
 <ul class="navbar-nav mr-auto">
 <li class="nav-item active">
 <a class="nav-link text-dark" href="/ ">All</a>
 </li>
 {% for category in categories %}
 <li class="nav-item">
 <a class="nav-link text-dark"
href="/?category={{category.id}}">{{category.name}}</
...........................
```

- **Finally, running the project and performing CRUD operations on Brand, Category and Product**

```
 python manage.py runserver
```

## **Conclusion**

For quick access to items, brands, and categories, we implemented a search bar. Additionally, a fresh bootstrap template was added to the website's front end.