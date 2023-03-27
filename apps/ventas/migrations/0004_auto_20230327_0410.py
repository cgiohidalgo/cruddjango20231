# Generated by Django 2.2.28 on 2023-03-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20230327_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='ciudad',
            field=models.CharField(choices=[('IBG', 'Ibague'), ('MED', 'Medellín'), ('CALI', 'Cali'), ('B/Q', 'Barranquilla'), ('BCM', 'Bucaramanga'), ('CUC', 'Cucuta'), ('SOAC', 'Soacha'), ('SOL', 'Soledad'), ('BOG', 'Bogotá'), ('CART', 'Cartagena')], default='CALI', max_length=4),
        ),
    ]