# Generated by Django 5.0.6 on 2024-07-16 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='producto',
        ),
    ]
