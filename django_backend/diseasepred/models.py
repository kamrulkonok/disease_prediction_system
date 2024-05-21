from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from users.models  import Patient, Doctor
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.m
# odels import AbstractUser
# from datetime import date
# from django.conf import settings


class Diabetes(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    bloodpressure = models.FloatField()
    skinthickness = models.FloatField()
    bmi = models.FloatField()
    insulin = models.FloatField()
    age = models.FloatField()
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.CharField(max_length=255)
    


class HeartDisease(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    age = models.FloatField()
    sex = models.FloatField()
    cp = models.FloatField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.FloatField()
    restecg = models.FloatField()
    thalach = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    ca = models.FloatField()
    thal = models.FloatField()
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.CharField(max_length=255)
   

class BreastCancer(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    radius_mean = models.FloatField()
    texture_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    area_mean =  models.FloatField()
    smoothness_mean = models.FloatField()
    compactness_mean = models.FloatField()
    concavity_mean = models.FloatField()
    concave_points_mean = models.FloatField()
    symmetry_mean = models.FloatField()
    fractal_dimension_mean = models.FloatField()
    radius_se = models.FloatField()
    texture_se = models.FloatField()
    perimeter_se = models.FloatField()
    area_se = models.FloatField()
    smoothness_se = models.FloatField()
    compactness_se = models.FloatField()
    concavity_se = models.FloatField()
    concave_points_se = models.FloatField()
    symmetry_se = models.FloatField()
    fractal_dimension_se = models.FloatField()
    radius_worst = models.FloatField()
    texture_worst = models.FloatField()
    perimeter_worst = models.FloatField()
    area_worst = models.FloatField()
    smoothness_worst = models.FloatField()
    compactness_worst = models.FloatField()
    concavity_worst = models.FloatField()
    concave_points_worst = models.FloatField()
    symmetry_worst = models.FloatField()
    fractal_dimension_worst = models.FloatField()
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.CharField(max_length=255)
    prediction = models.IntegerField(max_length=1)
    


class diseaseinfo(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diseasename = models.CharField(max_length = 200)
    no_of_symp = models.IntegerField()
    symptomsname = ArrayField(models.CharField(max_length=200))
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    consultdoctor = models.CharField(max_length = 200)

def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

class SkinCancer(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to=upload_to)
    prediction = models.IntegerField(max_length=1)

class consultation(models.Model):

    patient = models.ForeignKey(Patient ,null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor ,null=True, on_delete=models.CASCADE)
    diseaseinfo = models.OneToOneField(diseaseinfo, null=True, on_delete=models.SET_NULL)
    consultation_date = models.DateField()
    status = models.CharField(max_length = 20)
    




class rating_review(models.Model):

    patient = models.ForeignKey(Patient ,null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor ,null=True, on_delete=models.SET_NULL)
    
    rating = models.IntegerField(default=0)
    review = models.TextField( blank=True ) 


    @property
    def rating_is(self):
        new_rating = 0
        rating_obj = rating_review.objects.filter(doctor=self.doctor)
        for i in rating_obj:
            new_rating += i.rating
       
        new_rating = new_rating/len(rating_obj)
        new_rating = int(new_rating)
        
        return new_rating