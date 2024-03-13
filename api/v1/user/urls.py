from .views import RegisterViewSet, LoginView, LogoutViewSet, TokenCheckView
from django.urls import path

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/<str:token>/', TokenCheckView.as_view(), name='token'),
    path('logout/', LogoutViewSet.as_view({'post': 'create'}), name='logout'),
]