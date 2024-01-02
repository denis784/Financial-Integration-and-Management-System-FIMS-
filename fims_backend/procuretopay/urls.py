# procuretopay/urls.py
from django.urls import path
from .views import TenderList, TenderDetail, ResponseList, ResponseDetail

urlpatterns = [
    path('tenders/', TenderList.as_view(), name='tender-list'),
    path('tenders/<int:pk>/', TenderDetail.as_view(), name='tender-detail'),
    path('responses/', ResponseList.as_view(), name='response-list'),
    path('responses/<int:pk>/', ResponseDetail.as_view(), name='response-detail'),
]
