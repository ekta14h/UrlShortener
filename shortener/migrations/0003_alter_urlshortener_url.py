# Generated by Django 3.2.8 on 2022-05-02 08:18

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_urlshortener_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]