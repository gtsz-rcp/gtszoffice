# Generated by Django 2.0.5 on 2018-06-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(related_name='photo_items', to='photo.Photo'),
        ),
    ]
