# Generated by Django 5.0.6 on 2024-07-18 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Snake',
        ),
    ]