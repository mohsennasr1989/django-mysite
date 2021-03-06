# Generated by Django 3.1.5 on 2021-01-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210117_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='plural_unit',
            field=models.CharField(choices=[('Box', 'BOX'), ('Coil', 'COIL'), ('Bar', 'BAR')], default='box', help_text='Product plural unit', max_length=10),
        ),
        migrations.AlterField(
            model_name='products',
            name='singular_unit',
            field=models.CharField(choices=[('Pieces', 'PCS'), ('Meter', 'M')], default='pieces', help_text='Product singular unit', max_length=10),
        ),
    ]
