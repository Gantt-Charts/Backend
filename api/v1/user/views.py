from rest_framework import mixins, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api.models import User
from .permissions import ProjectPermission
from .serializer import UserSerializer, UserRegSerializer, ProfileSerializer


class CreateUserView(mixins.CreateModelMixin, GenericViewSet):
    """Регистрация пользователя."""
    def get_queryset(self):
        return User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegSerializer


class UserViewSet(ModelViewSet):
    """Пользователи."""
    queryset = User.objects.all()
    permission_classes = (ProjectPermission, IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserSerializer


class ProfileCreate(generics.GenericAPIView):
    """ Наполнение профиля юзера. """

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user.profile = serializer.save()
            return Response(ProfileSerializer(user.profile))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)