# Generated by Django 3.1.5 on 2021-01-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('PIPE_FITTING', 'Pipe & Fittings'), ('VALVE', 'Valves'), ('MANIFOLD', 'Manifolds'), ('UFH', 'Underfloor Heating'), ('TOOL', 'Tools')], default='PIPE_FITTING', max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='plural_unit',
            field=models.CharField(choices=[('BOX', 'Box'), ('COIL', 'Coil'), ('BAR', 'Bar')], default='BOX', help_text='Product plural unit', max_length=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='singular_unit',
            field=models.CharField(choices=[('PCS', 'Pieces'), ('M', 'Meter')], default='PCS', help_text='Product singular unit', max_length=10),
        ),
    ]
