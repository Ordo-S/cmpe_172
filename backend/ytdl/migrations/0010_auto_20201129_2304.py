# Generated by Django 2.2 on 2020-11-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytdl', '0009_auto_20201129_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytdl',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]
