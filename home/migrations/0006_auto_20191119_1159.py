# Generated by Django 2.2.2 on 2019-11-19 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_video_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
