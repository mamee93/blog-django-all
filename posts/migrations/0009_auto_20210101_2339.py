# Generated by Django 3.1.4 on 2021-01-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210101_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='contents',
        ),
    ]
