from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import FootprintSerializer
from .models import Footprint

class FootprintList(generics.ListCreateAPIView):
    queryset = Footprint.objects.all()
    serializer_class = FootprintSerializer

class FootprintDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footprint.objects.all()
    serializer_class = FootprintSerializer
