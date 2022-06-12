Lab 1 E-Commerce
a. Objective
The overall objective of the lab is to create an e-commerce website. But, the first lab has the following objectives:

To install and create suitable running and compiling environments
To create superuser, users and run the server
To add modules and verify CRUD operation
b. Introduction
For this lab, we employ a variety of frameworks and settings. The IDE we used was VS Code, and the framework was Python/Django. An e-commerce website is one that allows users and sellers to buy and sell things over the internet. It is one of the most effective current company models. E-commerce platforms make purchasing goods and services easier. For this lab report, we will create an e-commerce website.

We also need to be aware of the various languages. Python is the most widely used programming language, thanks to its simple syntax and efficient structure. Django is a Python web-based open-source framework. Django has a lot of built-in models, which makes it easy to concentrate on the application's writing. VS Code is another option and versatile IDE out there.

Git is also used in this lab for source control. We can also use Github Desktop for commit'ing and push'ing the code into a repository on GitHub. That repository when made public can be shared with anyone .

c. Procedure
We did the following steps in this lab:

1. Initializing environment

We downloaded the software and environments required for the project. Those were:

Python
Pip
Sqlite
DBeaver
Django
VS Code
Github account
We had some of them already and set up the remaining. The software could be different in the case of different operating systems with the same functionality. We checked if everything was working as it should.

2. Migrating and creating users

After the environment setup, we started the project and migrated files.

Syntax: django-admin startproject ecommerce_sandeep cd ecommerce_sandeep python manage.py migrate

We ran the server if it was working. Then, we got the link for the server as 127.0.0.1:8000. Again, we verified the admin side using 127.0.0.1:8000/admin. We were able to create a superuser and other users.
Syntax: python manage.py runserver

3. Database verification and CRUD operations

Then, we added a module product_module and migrated files to the database. Now, we were able to do CRUD operations on the server. Syntax: python manage.py startapp product_module ……. python manage.py runserver

4. Source Control

Finally, we used Git for source control. We created a repository with the name ecommerce_sandeep and created a markdown file “lab1.md” which is this document. Then, we committed and pushed the code and folder to the repository. The repository is now available at: https://github.com/Sandeepbhatta/ecommerce_sandeep-1/tree/main/ecommerce_sandeep/lab_manual

d. Output
Installation of python| pip alt text

Creation of project folder alt text

Migration alt text

Creating superuser alt text

Running server alt text alt text

Logging In alt text

CRUD operation alt text

Git initialization alt text

e. Conclusion
We learned a lot from the first e-commerce lab. The initial setup aided us in quickly creating environments and setting up. Then we knew how to start a Django project. It was also learned how to operate the server. On the server, we knew how to perform CRUD operations. Finally, we learned more about Git and Github for source control. Our code was easily available after we created a Github repository and shared it.
