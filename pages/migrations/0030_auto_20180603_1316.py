# Generated by Django 2.0.5 on 2018-06-03 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_auto_20180603_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1527999389.8350892, max_length=20, unique=True),
        ),
    ]