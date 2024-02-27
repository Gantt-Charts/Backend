from rest_framework import serializers
from api.models import Task, Project





class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_by')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'type', 'start', 'end', 'progress', 'isDisabled', 'project')