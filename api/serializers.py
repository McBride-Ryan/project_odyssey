# api/serializers.py

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' # Include all fields from the Task model
        # Or specify fields: fields = ['id', 'title', 'description', 'completed']