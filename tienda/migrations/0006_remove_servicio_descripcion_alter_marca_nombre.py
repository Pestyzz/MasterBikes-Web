# Generated by Django 5.0.6 on 2024-06-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_marca_producto_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
