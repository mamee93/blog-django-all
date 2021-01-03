# Generated by Django 3.1.4 on 2021-01-02 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20210102_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='previous_post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.post'),
        ),
    ]
