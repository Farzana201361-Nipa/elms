from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, CourseMaterial, EnrollmentRequest

# Register your models here.


# Register your custom user model with Django's UserAdmin interface
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'user_type', 'is_staff', 'is_active')}
        ),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'faculty']
    search_fields = ['title', 'faculty__username']
    
    
@admin.register(CourseMaterial)    
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ['course', 'file', 'upload_date']
    search_fields = ['course__title']
    
    
@admin.register(EnrollmentRequest)
class EnrollmentRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'status', 'requested_at']
    list_filter = ['status']
    search_fields = ['student__username', 'course__title']
