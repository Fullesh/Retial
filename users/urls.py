from django.urls import path

from users.apps import UsersConfig
from users.views import UserRetrieveAPIView, UserCreateAPIView, UserDestroyAPIView, UserUpdateAPIView, UserListAPIView

app_name = UsersConfig.name
urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_view'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
]
