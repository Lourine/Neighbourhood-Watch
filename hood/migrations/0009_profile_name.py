# Generated by Django 3.1.2 on 2020-11-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20201102_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
