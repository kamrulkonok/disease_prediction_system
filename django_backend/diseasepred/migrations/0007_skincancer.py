# Generated by Django 3.2.4 on 2021-06-08 02:14

import diseasepred.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseasepred', '0006_auto_20210607_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=diseasepred.models.upload_to, verbose_name='Image')),
            ],
        ),
    ]
