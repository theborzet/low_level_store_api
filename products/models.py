from django.db import models
from uuid import uuid4

class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

class Token(models.Model):
    value = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)