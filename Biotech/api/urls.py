from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignUpApi, UserViewSet
"""
API endpoints:
- /api/users/: Получение информации о пользователе.

Authentication endpoints:
- /auth/signup/: Регистрация нового пользователя.
"""

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

auth_urls = [
    path('signup/', SignUpApi.as_view(), name='signup'),
]

urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include(auth_urls)),
]
