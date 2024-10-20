# Generated by Django 5.1 on 2024-08-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True)),
                ('name', models.CharField(max_length=65, verbose_name='Модель телефона')),
                ('image', models.URLField(default=None)),
                ('price', models.IntegerField(default=None)),
                ('release_date', models.DateField(default=None)),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug',  models.SlugField(default=None)),
            ],
        ),
    ]
