# Generated by Django 3.1.7 on 2021-07-01 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210701_1413'),
        ('diseasepred', '0009_auto_20210701_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='breastcancer',
            name='comment',
            field=models.CharField(default='You Have Cancer', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='confidence',
            field=models.DecimalField(decimal_places=2, default=70, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diabetes',
            name='comment',
            field=models.CharField(default='yOU HAVE CANCER', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diabetes',
            name='confidence',
            field=models.DecimalField(decimal_places=2, default=80, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heartdisease',
            name='comment',
            field=models.CharField(default='yOu have cancer', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heartdisease',
            name='confidence',
            field=models.DecimalField(decimal_places=2, default=80, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skincancer',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skincancer',
            name='prediction',
            field=models.IntegerField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
