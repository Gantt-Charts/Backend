from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from api.models import Task, Project, User
from api.v1.Gantt.serializer import ProjectSerializer, ProjectTaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        return self.queryset.filter(created_by__username=username)

    def perform_create(self, serializer):
        if self.request.user.username == self.kwargs.get('username'):
            serializer.save(created_by=self.request.user)
        else:
            raise permissions.PermissionDenied('You do not have permission to perform this action.')

class ProjectTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ProjectTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print(self.request)
        username = self.kwargs.get('username')
        project_id = self.kwargs.get('project_id')
        return self.queryset.filter(project__created_by__username=username, project_id=project_id)

    def perform_create(self, serializer):
        print(self.request)
        if self.request.user.username == self.kwargs.get('username'):
            project_id = self.kwargs.get('project_id')
            project = Project.objects.get(id=project_id, created_by=self.request.user)
            serializer.save(project=project)
        else:
            raise permissions.PermissionDenied('You do not have permission to perform this action.')
