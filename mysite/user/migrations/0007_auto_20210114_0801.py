# Generated by Django 3.1.5 on 2021-01-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210112_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_last_login_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]