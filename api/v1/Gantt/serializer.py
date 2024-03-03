from rest_framework import serializers
from api.models import Task, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_by')

class ProjectTaskSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'type', 'start', 'end', 'progress', 'isDisabled', 'project', 'dependencies')

    def get_dependencies(self, obj):
        tasks = Task.objects.filter(project=obj.project).exclude(id=obj.id)
        return [task.name for task in tasks]