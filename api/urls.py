from django.urls import path, include

urlpatterns = [
    path('', include('api.v1.Gantt.urls')),
    path('', include('api.v1.user.urls')),
]