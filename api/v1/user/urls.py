from .views import RegisterViewSet, LoginView, LogoutViewSet
from django.urls import path

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutViewSet.as_view({'post': 'create'}), name='logout'),
]