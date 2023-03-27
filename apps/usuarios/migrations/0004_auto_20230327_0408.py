# Generated by Django 2.2.28 on 2023-03-27 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20230327_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administradorduenio',
            name='tipo',
            field=models.CharField(choices=[('ADMIN', 'Administrador'), ('CEO', 'Duenio')], max_length=5),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipoDocumento',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('PAS', 'Pasaporte'), ('TI', 'Tarjeta de Identidad')], max_length=3),
        ),
    ]