# Generated by Django 2.2.5 on 2019-09-27 01:26

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190926_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
