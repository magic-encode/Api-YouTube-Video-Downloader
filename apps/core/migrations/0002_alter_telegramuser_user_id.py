# Generated by Django 4.1.7 on 2023-03-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]