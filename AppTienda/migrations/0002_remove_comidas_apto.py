# Generated by Django 4.1 on 2022-09-06 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comidas',
            name='apto',
        ),
    ]
