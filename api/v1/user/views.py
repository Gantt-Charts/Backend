from django.contrib.auth import logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializer import UserSerializer, LoginSerializer, User


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Автоматически войти в только что созданный аккаунт
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'username': user.username, 'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return user

class LoginView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=user, password=password)
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'username': user.username, 'token': token.key}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'User is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        token = request.auth
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)