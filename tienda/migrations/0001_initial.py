# Generated by Django 5.0.6 on 2024-07-16 01:31

import django.db.models.deletion
import tienda.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tipoaccesorio', models.CharField(choices=[('BICICLETA', 'BICICLETA'), ('CASCOS', 'CASCOS'), ('ROPA', 'ROPA'), ('ZAPATILLAS', 'ZAPATILLAS'), ('LUCES', 'LUCES'), ('CANDADOS', 'CANDADOS'), ('PORTA BICICLETAS', 'PORTA BICICLETAS'), ('OTROS', 'OTROS')], default='BICICLETA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tamanioaro', models.IntegerField(default=26)),
                ('suspension', models.CharField(choices=[('DELANTERA', 'DELANTERA'), ('TRASERA', 'TRASERA'), ('DOBLE', 'DOBLE')], default='DELANTERA', max_length=9)),
                ('marco', models.CharField(choices=[('ACERO', 'ACERO'), ('ALUMINIO', 'ALUMINIO'), ('CARBON', 'CARBON')], default='ACERO', max_length=8)),
                ('tipobicicleta', models.CharField(choices=[('MONTAÑA', 'MONTAÑA'), ('RUTA', 'RUTA'), ('BMX', 'BMX'), ('HIBRIDA', 'HIBRIDA'), ('CICLOCROSS', 'CICLOCROSS'), ('GRAVEL', 'GRAVEL'), ('ENDURO', 'ENDURO'), ('DOWNHILL', 'DOWNHILL')], default='MONTAÑA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='RUT')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', tienda.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('id_transaccion', models.CharField(max_length=100, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('comentarios', models.TextField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE'), ('E', 'ENVIADO'), ('R', 'RECIBIDO')], default='P', max_length=1)),
                ('boleta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.boleta')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('tipo_pago', models.CharField(choices=[('T', 'TRANSFERENCIA'), ('C', 'CREDITO'), ('D', 'DEBITO')], max_length=1)),
                ('estado', models.CharField(choices=[('P', 'PENDIENTE'), ('A', 'ACEPTADO'), ('R', 'RECHAZADO')], default='P', max_length=1)),
                ('codigo_autorizacion', models.CharField(blank=True, max_length=100, null=True)),
                ('boleta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.boleta')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('estado', models.CharField(choices=[('sin confirmar', 'SIN CONFIRMAR'), ('en preparacion', 'EN PREPARACION'), ('enviado', 'ENVIADO'), ('entregado', 'ENTREGADO'), ('devuelto', 'DEVUELTO'), ('rechazado', 'RECHAZADO'), ('cancelado', 'CANCELADO')], default='pendiente', max_length=20)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, upload_to='static/media/productos/')),
                ('accesorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.accesorio')),
                ('bicicleta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.bicicleta')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.marca')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='tienda.pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.boleta')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
