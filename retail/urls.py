from django.urls import path

from retail.apps import RetailConfig
from retail.views import NetworkRetrieveAPIView, NetworkListAPIView, NetworkUpdateAPIView, NetworkDeleteAPIView

app_name = RetailConfig.name

urlpatterns = [
    path('', NetworkListAPIView.as_view(), name='network_list'),
    path('network/<int:pk>/', NetworkRetrieveAPIView.as_view(), name='network_detail'),
    path('network/edit/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network_edit'),
    path('network/update/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network_update'),
    path('network/delete/<int:pk>/', NetworkDeleteAPIView.as_view(), name='network_delete'),
]
