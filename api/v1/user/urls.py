from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from api.v1.user.views import CreateUserView, UserViewSet

users_router = SimpleRouter()
users_router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='token'),
    path('v1/registration/', CreateUserView.as_view({'post': 'create'}),
         name='registration'),

    path('v1/', include(users_router.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)