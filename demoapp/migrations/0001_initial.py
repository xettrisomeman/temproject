# Generated by Django 3.0 on 2019-12-11 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_carousel_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/carosuel/Home')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
