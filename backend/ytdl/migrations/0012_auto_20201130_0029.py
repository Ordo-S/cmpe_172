# Generated by Django 2.2 on 2020-11-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytdl', '0011_auto_20201129_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdownloadhistory',
            options={},
        ),
        migrations.RemoveField(
            model_name='userdownloadhistory',
            name='test',
        ),
        migrations.AddField(
            model_name='userdownloadhistory',
            name='videos',
            field=models.ManyToManyField(to='ytdl.Ytdl'),
        ),
    ]