# Generated by Django 4.0 on 2023-05-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuales', '0014_imagenes_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='ciclo',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='ciclo',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mortalidad',
            name='ciclo',
            field=models.IntegerField(max_length=1000),
        ),
    ]
