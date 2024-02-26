from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('gantt/', include('api.v1.Gantt.urls')),
]