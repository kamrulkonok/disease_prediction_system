from django.db.models import fields
from rest_framework import serializers
from .models import Feedback, Chat

class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"