# Generated by Django 3.2.8 on 2022-04-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortener',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]