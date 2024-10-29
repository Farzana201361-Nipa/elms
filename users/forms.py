from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Course, EnrollmentRequest, Announcement

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'faculty']

class EnrollmentRequestForm(forms.ModelForm):
    class Meta:
        model = EnrollmentRequest  
        fields = []

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['course', 'content']
    
    