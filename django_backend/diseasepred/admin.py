from django.contrib import admin
from .models import HeartDisease, Diabetes, diseaseinfo, BreastCancer, SkinCancer, consultation, rating_review
# # Register your models here.
# admin.site.register(patient)
# admin.site.register(doctor)
admin.site.register(diseaseinfo)
admin.site.register(consultation)
admin.site.register(rating_review)
# admin.site.register(User)
admin.site.register(Diabetes)
admin.site.register(HeartDisease)
admin.site.register(BreastCancer)
admin.site.register(SkinCancer)