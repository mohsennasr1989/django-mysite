# Generated by Django 3.1.5 on 2021-01-23 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210120_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('id', 'user', 'firstname', 'lastname', 'cellphone'), 'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
    ]