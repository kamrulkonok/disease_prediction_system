from rest_framework import serializers
from .models import BreastCancer ,Diabetes, HeartDisease, diseaseinfo, consultation, rating_review, SkinCancer 
from users.models import Patient
from django.contrib.auth import get_user_model
# from rest_framework.authtoken.views import Token
# from chats.models import Chat, Feedback
# from django.contrib.auth import authenticate

User = get_user_model()
class BreastCancerSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = BreastCancer
        fields = "__all__"
        read_only_fields = [fields]
        #fields = ['radius_mean' ,'texture_mean' ,'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave_points_se','symmetry_se','fractal_dimension_se', 'radius_worst','texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst']
    # def create(self, validated_data):
    #     user = validated_data.pop('user')
    #     instance = BreastCancer.objects.create(
    #         user=user,
    #         **validated_data
    #     )
    #     return instance

class DiabetesSerializer(serializers.ModelSerializer):
    #patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = Diabetes
        fields = "__all__"
        read_only_fields = [fields]
        #fields = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'bmi', 'insulin', 'age']
    # def create(self, validated_data):
    #     patient = validated_data.pop('patient')
    #     instance = Diabetes.objects.create(
    #         patient=patient,
    #         **validated_data
    #     )
    #     return instance

class HeartDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        # patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
        model = HeartDisease
        #fields = "__all__"
        fields = ['patient','age','sex','cp','trestbps','chol', 'fbs', 'restecg', 'thalach', 'exang','oldpeak','slope', 'ca','thal']
        read_only_fields = [fields]
    def create(self, validated_data):
        user = validated_data.pop('user')
        pat = Patient.objects.filter(user = user).first()
        instance = HeartDisease(
            patient = pat,
            **validated_data
        )
        instance.save()
        return instance
    
class SkinCancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinCancer
        exclude = ['patient','prediction']
        


    # def create(self, validated_data):
    #     patient = validated_data.pop('patient')
    #     instance = HeartDisease.objects.create(
    #         patient=patient,
    #         **validated_data
    #     )
    #     return instance



# class ChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#         fields = ['created','consultation','sender','message']

# class FeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = ['created','sender','feedback']



class diseaseinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = diseaseinfo
        fields = ['patient','diseasename', 'no_of_symp', 'symptomsname', 'confidence','consultdoctor']
    def create(self, validated_data):
        #user = validated_data.pop('user')
        instance = diseaseinfo.objects.create(
            #user=user,
            **validated_data
        )
        return instance

class consultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultation
        fields = ['patient', 'doctor', 'diseaseinfo', 'consultation_date', 'status']


class rating_reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating_review
        fields = ['patient', 'doctor', 'rating', 'review']
        

