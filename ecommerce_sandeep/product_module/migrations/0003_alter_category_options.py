# Generated by Django 4.0.4 on 2022-06-10 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
