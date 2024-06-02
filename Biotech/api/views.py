from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from celery_app import send_otp_email
from .serializers import (RegistrationSerializer,
                          UserMeSerializer,
                          UsersSerializer
                          )


User = get_user_model()


class SignUpApi(APIView):
    """
    Регистрация нового пользователя.
    Отправка OTP кода через Celery

    Возвращает данные нового пользователя с HTTP статусом 200 в случае успеха,
    либо сообщение об ошибке с соответствующим HTTP статусом в случае неудачи.
    """

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_otp_email.delay(user.id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):

    """
    Получение и редактирование информации о пользователе.

    Конечные точки:
    - GET /api/users/: Получение информации о пользователе.
    - PATCH /api/users/: Редактирование информации о пользователе.
    - DELETE /api/users/: Удаление пользователя.
    - GET /api/users/me/: Получение и редактирование информации о текущем пользователе.
    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(
        methods=['GET', 'PATCH', ],
        detail=False,
        permission_classes=(IsAuthenticated,),
        url_path='me')
    def get_user(self, request):
        try:
            user = get_object_or_404(User, username=self.request.user)
            if request.method == 'GET':
                serializer = UserMeSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if request.method == 'PATCH':
                serializer = UserMeSerializer(user,
                                              data=request.data,
                                              partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
