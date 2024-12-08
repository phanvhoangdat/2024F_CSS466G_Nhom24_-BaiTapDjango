from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    
    ROLE_CHOICES = [
        ('admin', 'Quản trị viên'),
        ('user', 'Người dùng bình thường'),
        ('content_manager', 'Người quản lý nội dung'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username
