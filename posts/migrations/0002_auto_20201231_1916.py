# Generated by Django 3.1.4 on 2020-12-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='Profile_img',
            field=models.ImageField(upload_to='Profile_img/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='post/'),
        ),
    ]
