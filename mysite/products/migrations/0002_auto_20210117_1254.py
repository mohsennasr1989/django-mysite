# Generated by Django 3.1.5 on 2021-01-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='package_quantity',
            field=models.IntegerField(default=1, help_text='Product package quantity'),
        ),
    ]
