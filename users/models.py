from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
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
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    faculty = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 'faculty'})
 
    
    def __str__(self):
        return self.title
 
#Creating CourseMaterial model to upload multiple file in one course   
class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="materials" )
    file = models.FileField(upload_to='course_materials/')
    upload_date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"{self.course.title} - {self.file.name}"
   
   
class EnrollmentRequest(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.student.username} - {self.course.title} - {self.status}"
   
   
class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="announcements")
    faculty = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 'faculty'})
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement for {self.course.title} by {self.faculty.username}"

        
    
    
    

