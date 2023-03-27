# Generated by Django 2.2.28 on 2023-03-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20230327_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='ciudad',
            field=models.CharField(choices=[('CART', 'Cartagena'), ('SOAC', 'Soacha'), ('BCM', 'Bucaramanga'), ('CALI', 'Cali'), ('SOL', 'Soledad'), ('CUC', 'Cucuta'), ('IBG', 'Ibague'), ('BOG', 'Bogotá'), ('B/Q', 'Barranquilla'), ('MED', 'Medellín')], default='CALI', max_length=4),
        ),
        migrations.AlterField(
            model_name='pagoscredito',
            name='entidadAprobacion',
            field=models.CharField(choices=[('AX', 'AMERICANEXPRESS'), ('VI', 'VISA'), ('CA', 'MASTERCARD')], max_length=2),
        ),
    ]