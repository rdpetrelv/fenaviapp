# Generated by Django 4.0 on 2023-03-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productor', models.CharField(max_length=1000)),
                ('ciclo', models.CharField(max_length=1000)),
                ('sexo', models.CharField(max_length=1000)),
                ('semana', models.IntegerField()),
                ('consumo_ave', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('peso_ave', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('c_a_acum', models.DecimalField(decimal_places=50, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Cicloproduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productor', models.CharField(max_length=1000)),
                ('ciclo', models.CharField(max_length=1000)),
                ('dias_ciclo', models.IntegerField()),
                ('lote', models.CharField(max_length=1000)),
                ('raza', models.CharField(max_length=1000)),
                ('sexo', models.CharField(max_length=1000)),
                ('aves_iniciales', models.IntegerField()),
                ('aves_finales', models.IntegerField()),
                ('peso_inicial_gramos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('peso_final_gramos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('consumo_total_ave_kilogramos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('tasa_mortalidad_total', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('consumo_total_kilogramos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('total_bultos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('peso_vivo_total_kilogramos', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('conversion_acumulada', models.DecimalField(decimal_places=50, max_digits=1000)),
                ('indice_productividad', models.DecimalField(decimal_places=50, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mortalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productor', models.CharField(max_length=1000)),
                ('ciclo', models.CharField(max_length=1000)),
                ('sexo', models.CharField(max_length=1000)),
                ('semana', models.IntegerField()),
                ('dia', models.IntegerField()),
                ('mort_aves', models.IntegerField()),
                ('selec_aves', models.IntegerField()),
                ('total_mortalidad_aves', models.IntegerField()),
                ('mortalidad_acumulada', models.IntegerField()),
                ('saldo_aves', models.IntegerField()),
            ],
        ),
    ]