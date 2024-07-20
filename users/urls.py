from django.urls import path

from users.apps import UsersConfig
from users.views import UserRetrieveAPIView

app_name = UsersConfig.name
urlpatterns = [
    path('', UserRetrieveAPIView.as_view(), name='user_detail'),
]
