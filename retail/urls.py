from django.urls import path

from retail.apps import RetailConfig
from retail.views import NetworkRetrieveAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('', NetworkRetrieveAPIView.as_view(), name='network_list'),
]
