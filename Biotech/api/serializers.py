from rest_framework import serializers

from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра пользователей.
    """
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio',)


class UserMeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра и редактирования информации о текущем пользователе.
    """
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio')


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации нового пользователя.
    """
    class Meta:
        model = User
        fields = ('email', 'username')
        """
        Проверка поля username на допустимость значения.
        """
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Использовать me в качестве поля username нельзя!')
        return value
