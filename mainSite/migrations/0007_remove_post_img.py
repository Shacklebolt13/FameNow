# Generated by Django 3.2.4 on 2021-07-13 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0006_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]
