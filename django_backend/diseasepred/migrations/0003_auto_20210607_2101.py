# Generated by Django 3.2.4 on 2021-06-07 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseasepred', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breastcancer',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='diabetes',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='diseaseinfo',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='heartdisease',
            name='patient',
        ),
    ]
