# Generated by Django 2.0.5 on 2018-06-06 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0002_auto_20180606_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-pub_date',)},
        ),
    ]