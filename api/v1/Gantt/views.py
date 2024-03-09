from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from api.models import Task, Project, User
from api.v1.Gantt.serializer import ProjectSerializer, ProjectTaskSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        return self.queryset.filter(created_by__username=username)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, IsOwner]
        elif self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

class ProjectTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ProjectTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        project_id = self.kwargs.get('project_id')
        return self.queryset.filter(project__created_by__username=username, project_id=project_id)

    def perform_create(self, serializer):
        if self.request.user.username == self.kwargs.get('username'):
            project_id = self.kwargs.get('project_id')
            project = Project.objects.get(id=project_id, created_by=self.request.user)
            serializer.save(project=project)
            instance = serializer.save(project=project)
            return Response({'id': instance.id})
        else:
            raise permissions.PermissionDenied('You do not have permission to perform this action.')

    def perform_update(self, serializer):
        instance = serializer.save()
        return Response({'id': instance.id})

    def perform_destroy(self, instance):
        instance_id = instance.id
        instance.delete()
        return Response({'id': instance_id})
