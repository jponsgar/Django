# Generated by Django 5.0.6 on 2024-09-15 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_factura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='producto',
            new_name='nombre',
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.producto')),
            ],
        ),
    ]
