# Generated by Django 3.2.4 on 2021-07-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('title_es', models.CharField(default=None, max_length=200, unique=True)),
                ('description', models.TextField()),
                ('description_es', models.TextField(default=None)),
                ('technology', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects_images')),
            ],
        ),
    ]
