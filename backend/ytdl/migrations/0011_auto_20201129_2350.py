# Generated by Django 2.2 on 2020-11-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ytdl', '0010_auto_20201129_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdownloadhistory',
            options={'ordering': ['test']},
        ),
    ]
