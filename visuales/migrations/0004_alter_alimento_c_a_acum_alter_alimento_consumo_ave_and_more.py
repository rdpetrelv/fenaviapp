# Generated by Django 4.0 on 2023-03-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visuales', '0003_remove_mortalidad_dia_remove_mortalidad_mort_aves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='c_a_acum',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='consumo_ave',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='peso_ave',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='consumo_total_ave_kilogramos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='consumo_total_kilogramos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='conversion_acumulada',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='indice_productividad',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='peso_final_gramos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='peso_inicial_gramos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='peso_vivo_total_kilogramos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='tasa_mortalidad_total',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='cicloproduccion',
            name='total_bultos',
            field=models.DecimalField(decimal_places=5, max_digits=1000),
        ),
    ]
