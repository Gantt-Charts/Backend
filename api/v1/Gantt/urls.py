from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from api.v1.Gantt.views import TaskViewSet, ProjectViewSet

app_name = 'api'
users_router = SimpleRouter()
users_router.register(r'projects', ProjectViewSet, basename='project')
users_router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('v1/', include(users_router.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)