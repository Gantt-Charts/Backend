from rest_framework import serializers
from api.models import Task, Project

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_by')

class ProjectTaskSerializer(serializers.ModelSerializer):
    dependencies = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'type', 'start', 'end', 'progress', 'isDisabled', 'project', 'dependencies')

    def create(self, validated_data):
        dependencies = validated_data.pop('dependencies')
        task = Task.objects.create(**validated_data)
        task.dependencies.set(dependencies)
        task.save()
        return task

    def update(self, instance, validated_data):
        dependencies = validated_data.pop('dependencies')
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.start = validated_data.get('start', instance.start)
        instance.end = validated_data.get('end', instance.end)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.isDisabled = validated_data.get('isDisabled', instance.isDisabled)
        instance.project = validated_data.get('project', instance.project)
        instance.dependencies.set(dependencies)
        instance.save()
        return instance