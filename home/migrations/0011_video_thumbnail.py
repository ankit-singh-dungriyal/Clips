# Generated by Django 2.2.7 on 2019-11-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191122_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
