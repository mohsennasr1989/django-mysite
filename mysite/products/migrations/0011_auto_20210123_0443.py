# Generated by Django 3.1.5 on 2021-01-23 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_merge_20210123_0443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id', 'code', 'name', 'specification', 'size'), 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]