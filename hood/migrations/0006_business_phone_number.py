# Generated by Django 3.1.2 on 2020-11-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_auto_20201102_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]