from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.Gantt.views import TaskViewSet, ProjectViewSet

app_name = 'api'
users_router = SimpleRouter()
users_router.register('projects', ProjectViewSet, basename='project')
users_router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('v1/', include(users_router.urls)),
    path('v1/project/<int:pk>/tasks/', TaskViewSet.as_view({'get': 'list'}), name='tasks'),
]
urlpatterns = format_suffix_patterns(urlpatterns)