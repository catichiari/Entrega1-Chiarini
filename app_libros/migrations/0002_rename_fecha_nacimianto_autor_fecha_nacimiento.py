# Generated by Django 4.1.1 on 2022-09-12 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='fecha_nacimianto',
            new_name='fecha_nacimiento',
        ),
    ]
