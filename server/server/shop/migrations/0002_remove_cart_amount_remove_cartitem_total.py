# Generated by Django 5.1 on 2024-08-22 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
    ]
