# Generated by Django 5.1.1 on 2024-09-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_articletag_tag_articletag_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'ordering': ['-is_main']},
        ),
    ]
