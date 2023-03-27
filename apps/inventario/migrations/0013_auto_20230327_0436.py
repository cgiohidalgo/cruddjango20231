# Generated by Django 2.2.28 on 2023-03-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_auto_20230327_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ciudad',
            field=models.CharField(choices=[('BCM', 'Bucaramanga'), ('CUC', 'Cucuta'), ('BOG', 'Bogotá'), ('MED', 'Medellín'), ('SOAC', 'Soacha'), ('CALI', 'Cali'), ('IBG', 'Ibague'), ('CART', 'Cartagena'), ('B/Q', 'Barranquilla'), ('SOL', 'Soledad')], default='CALI', max_length=4),
        ),
        migrations.AlterField(
            model_name='detallesproducto',
            name='color',
            field=models.CharField(choices=[('Rojo', 'Rojo'), ('Morado', 'Morado'), ('Rosado', 'Rosado'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'), ('Beige', 'Beige'), ('Gris', 'Gris'), ('Marron', 'Marrón'), ('Otros', 'Otro'), ('Negro', ' Negro'), ('Blanco', 'Blanco'), ('Azul', 'Azul')], max_length=64),
        ),
        migrations.AlterField(
            model_name='detallesproducto',
            name='talla',
            field=models.CharField(choices=[('XL', 'xl'), ('M', 'm'), ('XS', 'xs'), ('L', 'l'), ('S', 's')], max_length=32),
        ),
    ]