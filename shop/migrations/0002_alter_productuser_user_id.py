# Generated by Django 4.1.5 on 2023-03-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productuser',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]