from django.urls import path 
from . import views
from .views import create_course, request_enrollment, course_list,approve_enrollment

app_name = "users"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/request/', views.request_enrollment, name='request_enrollment'),
    
    path('request-enrollment/<int:course_id>/', views.request_enrollment, name='request_enrollment'),
    path('approve-enrollment/<int:enrollment_id>/', views.approve_enrollment, name='approve_enrollment'),
]
