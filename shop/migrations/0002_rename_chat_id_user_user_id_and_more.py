# Generated by Django 4.1.5 on 2023-02-28 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='chat_id',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='shop.productuser'),
        ),
    ]
