# Generated by Django 2.0.5 on 2018-05-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20180527_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1527403378.8213067, max_length=20, unique=True),
        ),
    ]
