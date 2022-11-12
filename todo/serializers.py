from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'created_on', 'user', 'done']
        read_only_fields = ['user', 'created_on']


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        print(password)
        user = User.objects.create_user(
            validated_data['username'],
        )
        user.set_password(password)
        user.save()
        return user
