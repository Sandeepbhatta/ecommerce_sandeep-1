Lab 1 E-Commerce
a. Objective
The overall objective of the lab is to create an e-commerce website. But, the first lab has the following objectives:

To install and create suitable running and compiling environments
To create superuser, users and run the server
To add modules and verify CRUD operation
b. Introduction
We use different frameworks and environments for this lab. We have used VS Code as the IDE and Python/Django as the framework. An E-commerce website is a website that helps customers and sellers in buying/selling their products on the online platform. It is one of the best modern ways of business. E-commerce websites simplify the buying process of goods and services. We will be creating an e-commerce website for this lab report.

Additionally, we also need to know about the languages. Python is the most popular programming language with easy understanding and efficient structure. We use Django, a web-based open-source framework of Python. Django comes with many inbuilt models which makes us easier to focus on the writing part of the application. And VS Code is one of the most versatile IDE out there.

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

Syntax: django-admin startproject ecommerce_barun cd ecommerce_barun python manage.py migrate

We ran the server if it was working. Then, we got the link for the server as 127.0.0.1:8000. Again, we verified the admin side using 127.0.0.1:8000/admin. We were able to create a superuser and other users. Syntax: python manage.py runserver

3. Database verification and CRUD operations

Then, we added a module product_module and migrated files to the database. Now, we were able to do CRUD operations on the server. Syntax: python manage.py startapp product_module ……. python manage.py runserver

4. Source Control

Finally, we used Git for source control. We created a repository with the name ecommerce_barun and created a markdown file “lab1.md” which is this document. Then, we committed and pushed the code and folder to the repository. The repository is now available at: https://github.com/thebarunsharma/ecommerce_barun/

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
The first lab of e-commerce taught us many things. Initial setup helped us create environments and setup efficiently. Then, we knew how to start a project using Django. Knowledge about running the server was also obtained. We knew how to do CRUD operations on the server. Finally, we also knew more about source control using Git and Github. Making a repository on Github and sharing it made our code easily accessible.
