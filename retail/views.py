from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from retail.models import Network
from retail.serializers import NetworkSerializer


# Create your views here.

class NetworkRetrieveAPIView(RetrieveAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

