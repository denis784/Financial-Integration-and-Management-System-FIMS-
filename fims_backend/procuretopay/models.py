# procuretopay/models.py
from django.db import models

class Tender(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as per your requirements

class Response(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    # Add other fields as needed
