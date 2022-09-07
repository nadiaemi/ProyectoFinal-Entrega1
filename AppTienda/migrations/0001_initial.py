# Generated by Django 4.1 on 2022-09-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('apto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('apto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Otros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]