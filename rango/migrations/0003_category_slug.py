# Generated by Django 2.2.26 on 2022-01-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20220126_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
