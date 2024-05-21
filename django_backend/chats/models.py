from django.db import models
from django.contrib.auth import get_user_model
from diseasepred.models import consultation
User = get_user_model()

# Create your models here.

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    consultation_id =  models.ForeignKey(consultation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __unicode__(self):
        return self.message




class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __unicode__(self):
        return self.feedback