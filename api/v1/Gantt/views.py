from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics

from api.models import Task, Project
from api.v1.Gantt.serializer import ProjectSerializer, TaskSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectTaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Task.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        serializer.save(project_id=project_id)


# class ProjectViewSet(viewsets.ViewSet):
#     def list(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         project = get_object_or_404(Project, pk=pk)
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         project = get_object_or_404(Project, pk=pk)
#         serializer = ProjectSerializer(project, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         project = get_object_or_404(Project, pk=pk)
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class TaskListView(APIView):
#     def get(self, request, project_id):
#         project = Project.objects.get(id=project_id)
#         tasks = project.tasks.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
# class TaskDetailView(APIView):
#     def get(self, request, project_id, task_id):
#         project = Project.objects.get(id=project_id)
#         task = project.tasks.get(id=task_id)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
# class TaskCreateView(APIView):
#     def post(self, request, project_id):
#         project = Project.objects.get(id=project_id)
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(project=project)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class TaskUpdateView(APIView):
#     def put(self, request, project_id, task_id):
#         project = Project.objects.get(id=project_id)
#         task = project.tasks.get(id=task_id)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class TaskCompleteView(APIView):
#     def put(self, request, project_id, task_id):
#         project = Project.objects.get(id=project_id)
#         task = project.tasks.get(id=task_id)
#         task.complete = True
#         task.save()
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)