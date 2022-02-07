from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
#from django.contrib.auth.models import User
from demo_api import models

class UserSerializer(ModelSerializer):
    name=serializers.CharField(max_length=255)
    email=serializers.EmailField()
    password=serializers.CharField(
        style={'input_type':'password'},
        write_only=True
    )
    class Meta:
        model=models.CustomUser
        fields=['id','name','email','password']

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            email= validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance,validated_data)

