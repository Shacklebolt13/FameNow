# Generated by Django 3.2.4 on 2021-07-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0002_alter_user_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='bio',
            field=models.TextField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
