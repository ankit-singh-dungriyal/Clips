# Generated by Django 2.2.2 on 2019-11-19 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20191119_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
