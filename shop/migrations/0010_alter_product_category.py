# Generated by Django 4.1.5 on 2023-03-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='category', to='shop.category'),
        ),
    ]
