from rest_framework import serializers
from Gantt_Models.models import User, Profile


class UserRegSerializer(serializers.ModelSerializer):
    """Сериалайзер регистрации."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)

    def create(self, validated_data):
        """Сохранение пользователи в модели User."""
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер пользователей."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'date_joined',)
        read_only_fields = ('date_joined', 'is_staff',)

class UserAdminSerializer(serializers.ModelSerializer):
    """Сериалайзер пользователей администратора."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'date_joined',)
        read_only_fields = ('date_joined',)



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = [
            'user'
        ]
    def create(self, validated_data):
        profile = Profile.objects.create(user=self.context['request'].user,
                                         **validated_data)
        return profile