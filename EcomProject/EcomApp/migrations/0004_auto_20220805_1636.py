# Generated by Django 3.2.14 on 2022-08-05 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0003_auto_20220803_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
