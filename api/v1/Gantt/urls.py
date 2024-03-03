from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.Gantt.views import ProjectViewSet, ProjectTaskViewSet

app_name = 'api'
users_router = SimpleRouter()

urlpatterns = [
    path('projects/<str:username>/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'}), name='project_list'),
    path('projects/<str:username>/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='project_detail'),
    path('projects/<str:username>/<int:project_id>/tasks/', ProjectTaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='project_task_list'),
    path('projects/<str:username>/<int:project_id>/tasks/<int:pk>/', ProjectTaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='project_task_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)