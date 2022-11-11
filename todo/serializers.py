from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'created_on', 'user', 'done']
        read_only_fields = ['user', 'created_on']
