# Generated by Django 4.1 on 2022-08-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
