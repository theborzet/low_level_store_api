from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4




class CustomUser(AbstractUser):
    token = models.UUIDField(unique=False, editable=False, null=True)
    
    class Meta:
        unique_together = ['username']

class Token(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_tokens')
    value = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

CustomUser.groups.field.remote_field.related_name = 'customuser_set'
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_set'