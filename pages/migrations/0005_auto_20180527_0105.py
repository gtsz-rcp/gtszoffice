# Generated by Django 2.0.5 on 2018-05-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180527_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1527350707.8359141, max_length=20, unique=True),
        ),
    ]
