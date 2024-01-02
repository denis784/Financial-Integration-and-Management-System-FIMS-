# procuretopay/views.py
from rest_framework import generics
from .models import Tender, Response
from .serializers import TenderSerializer, ResponseSerializer

class TenderList(generics.ListCreateAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class TenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class ResponseList(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
