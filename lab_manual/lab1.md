# Lab 1 E-Commerce


## a. Objective

The lab's overall goal is to establish an e-commerce website. However, the first lab has the following goals:
1. Set up and configure appropriate running and compilation environments.
2. Create a superuser and users, as well as launch the server
3. Adding modules and testing CRUD operations

## b. Introduction

For this lab, we employ a variety of frameworks and settings. The IDE was Visual Studio Code, and the framework was Python/Django. An e-commerce website is one that allows users and sellers to buy and sell things over the internet. It is one of the most effective current company models. E-commerce platforms make purchasing goods and services easier. For this lab report, we will create an e-commerce website.

We also need to be familiar with the languages. Python is the most widely used programming language, thanks to its simple syntax and efficient structure. Django is a Python web-based open-source framework. Django has a lot of built-in models that let us focus on the writing side of the application. VS Code is also one of the most versatile IDEs available.

This lab also uses Git for source control. We may also utilize Github Desktop to commit and push our code to a GitHub repository. When the repository is made public, anyone can access it.

## c. Procedure
We did the following steps in this lab:

*1. Initializing environment*

We downloaded the software and environments required for the project. Those were:
* Python
* Pip
* DBeaver
* Sqlite
* VS Code
* Django
* Github account

We had some and were able to set up the rest. In the case of several operating systems with the same functionality, the software could be different. We double-checked that everything was in functioning order.

*2. Migrating and creating users*

We initiated the program and imported files after setting up the environment.

Syntax: 
*django-admin startproject ecommerce_sandeep  
cd ecommerce_sandeep  
python manage.py migrate* 

We ran the server if it was working.Then we got the server's link, which was 127.0.0.1:8000. Using 127.0.0.1:8000/admin, we confirmed the admin side once more. We were successful in establishing a superuser and other users.
Syntax: python manage.py runserver 

*3. Database verification and CRUD operations*

After that, we created a product module module and moved files to the database. We could now do CRUD tasks on the server.
Syntax: *python manage.py startapp product_module
…….
python manage.py runserver*

*4. Source Control*

Finally, for source control, we used Git. We built a repository called ecommerce sandeep and a markdown file called "lab1.md" that contains this document. The code and folder were then committed and published to the repository. The repository can now be found at:
https://github.com/Sandeepbhatta/ecommerce_sandeep-1
## d. Output

1. Installation of python| pip

2. Creation of project folder

4. Migration



5. Creating superuser

5. Running server


6. Logging In


8. CRUD operation


10. Git initialization


## e. Conclusion 

We learned a lot from the first e-commerce lab. The initial setup aided us in quickly creating environments and setting up. Then we knew how to start a Django project. It was also learned how to operate the server. On the server, we knew how to perform CRUD operations. Finally, we learned more about Git and Github for source control. Our code was easily available after we created a Github repository and shared it.
