# Generated by Django 5.0.6 on 2024-09-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cliente_rename_nombre_producto_producto_factura'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Factura',
        ),
    ]
