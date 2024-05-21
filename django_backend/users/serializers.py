from .models import Patient, Doctor
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import Token
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'user_name','first_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class DoctorRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Doctor
        fields = ('user', 'dob', 'registration_no','year_of_registration','qualification','State_Medical_Council','specialization')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data['user']['email'],
                                        validated_data['user']['user_name'],
                                        validated_data['user']['password'],
                                        validated_data['user']['first_name'],
                                        is_doctor=True,
                                        )
        doc = Doctor.objects.create(user=user, 
                                       registration_no=validated_data.pop('registration_no'),
                                       year_of_registration=validated_data.pop('year_of_registration'),
                                       qualification=validated_data.pop('qualification'),
                                       State_Medical_Council=validated_data.pop('State_Medical_Council'),
                                       specialization=validated_data.pop('specialization'),
                                       dob = validated_data.pop('dob'),
                                       )
        return doc

class PatientRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    
    class Meta:
        model = Patient
        fields = ('user','dob')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data['user']['email'],
                                        validated_data['user']['user_name'],
                                        validated_data['user']['first_name'],
                                        validated_data['user']['password'],
                                        is_patient=True)
        pat = Patient.objects.create(user=user, dob=validated_data.pop('dob'))
        return pat


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user', 'name','dob', 'address','mobile_no','gender']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'name','dob', 'address','mobile_no','gender', 'registration_no','year_of_registration','qualification','State_Medical_Council','specialization','rating']
