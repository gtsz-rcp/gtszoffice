# Generated by Django 2.0.5 on 2018-05-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20180527_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1527404103.8460886, max_length=20, unique=True),
        ),
    ]
