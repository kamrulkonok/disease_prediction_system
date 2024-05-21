# Generated by Django 3.2.4 on 2021-06-07 20:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreastCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius_mean', models.FloatField()),
                ('texture_mean', models.FloatField()),
                ('perimeter_mean', models.FloatField()),
                ('area_mean', models.FloatField()),
                ('smoothness_mean', models.FloatField()),
                ('compactness_mean', models.FloatField()),
                ('concavity_mean', models.FloatField()),
                ('concave_points_mean', models.FloatField()),
                ('symmetry_mean', models.FloatField()),
                ('fractal_dimension_mean', models.FloatField()),
                ('radius_se', models.FloatField()),
                ('texture_se', models.FloatField()),
                ('perimeter_se', models.FloatField()),
                ('area_se', models.FloatField()),
                ('smoothness_se', models.FloatField()),
                ('compactness_se', models.FloatField()),
                ('concavity_se', models.FloatField()),
                ('concave_points_se', models.FloatField()),
                ('symmetry_se', models.FloatField()),
                ('fractal_dimension_se', models.FloatField()),
                ('radius_worst', models.FloatField()),
                ('texture_worst', models.FloatField()),
                ('perimeter_worst', models.FloatField()),
                ('area_worst', models.FloatField()),
                ('smoothness_worst', models.FloatField()),
                ('compactness_worst', models.FloatField()),
                ('concavity_worst', models.FloatField()),
                ('concave_points_worst', models.FloatField()),
                ('symmetry_worst', models.FloatField()),
                ('fractal_dimension_worst', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.FloatField()),
                ('glucose', models.FloatField()),
                ('bloodpressure', models.FloatField()),
                ('skinthickness', models.FloatField()),
                ('bmi', models.FloatField()),
                ('insulin', models.FloatField()),
                ('age', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='diseaseinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=200)),
                ('no_of_symp', models.IntegerField()),
                ('symptomsname', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('confidence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consultdoctor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeartDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('sex', models.FloatField()),
                ('cp', models.FloatField()),
                ('trestbps', models.FloatField()),
                ('chol', models.FloatField()),
                ('fbs', models.FloatField()),
                ('restecg', models.FloatField()),
                ('thalach', models.FloatField()),
                ('exang', models.FloatField()),
                ('oldpeak', models.FloatField()),
                ('slope', models.FloatField()),
                ('ca', models.FloatField()),
                ('thal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='rating_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('review', models.TextField(blank=True)),
            ],
        ),
    ]