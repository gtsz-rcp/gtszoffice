# Generated by Django 2.0.5 on 2018-06-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_auto_20180606_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1528220565.9281156, max_length=20, unique=True),
        ),
    ]