from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USER_TYPES =[
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    user_type = models.CharField(choices=USER_TYPES, max_length=10, default='student')
    
    def __str__(self):
        return f"{self.email}({self.get_user_type_display()})"
    

    