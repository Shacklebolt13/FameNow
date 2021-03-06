# Generated by Django 3.2.4 on 2021-07-13 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0005_auto_20210710_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default='', max_length=250)),
                ('img', models.ImageField(upload_to='images/useruploads/post')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainSite.user')),
            ],
        ),
    ]
