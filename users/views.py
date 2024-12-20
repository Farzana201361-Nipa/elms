from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import Course, CourseMaterial, EnrollmentRequest
from .forms import CustomUserCreationForm, CourseForm, EnrollmentRequestForm, AnnouncementForm
from django.shortcuts import get_object_or_404



# Create your views here.

# Register view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('lms:home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lms:home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def is_faculty(user):
    return  user.is_authenticated and user.user_type == 'faculty'

def is_admin(user):
    return user.is_staff

@user_passes_test(is_faculty)
@login_required  
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.faculty = request.user
            course.save()
            return redirect('users:course_list')
        
    else:
        form = CourseForm()
    return render(request,'users/create_course.html', {'form': form})
    
    
@login_required
def request_enrollment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = EnrollmentRequestForm(request.POST)
        if form.is_valid():
            enrollment_request = form.save(commit=False)
            enrollment_request.student = request.user
            enrollment_request.course = course
            enrollment_request.save()
            return redirect('users:course_list')  
    else:
        form = EnrollmentRequestForm()
    return render(request, 'users/request_enrollment.html', {'form': form, 'course': course})

@login_required
@user_passes_test(is_admin)
def approve_enrollment(request, enrollment_id):
    
    pass


@login_required
def course_list(request):
    #fetching courses
    courses = Course.objects.all()  
    return render(request, 'users/course_list.html', {'courses': courses})



@login_required
@user_passes_test(is_admin)
def approve_enrollment(request, enrollment_id):
    enrollment_request = get_object_or_404(EnrollmentRequest, id=enrollment_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            enrollment_request.status = 'approved'
        elif action == 'decline':
            enrollment_request.status = 'declined'
        enrollment_request.save()
        return redirect('users:course_list') 
    
    return render(request, 'users/approve_enrollment.html', {'enrollment_request': enrollment_request})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("lms:home")



def student_content_view(request):
    if request.user.is_authenticated and request.user.user_type == 'student':
        approved_courses = Course.objects.filter(
            enrollmentrequest__student=request.user,
            enrollmentrequest__status='approved'
        )
        return render(request, 'users/student_content.html', {'approved_courses': approved_courses})
    else:
        return redirect('users:login')
    
    
    
@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.faculty = request.user  
            announcement.save()
            return redirect('users:view_announcements')  
    else:
        form = AnnouncementForm()
    
    return render(request, 'users/create_announcement.html', {'form': form})





@login_required
def view_announcements(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    announcements = course.announcements.all()
    return render(request, 'users/view_announcements.html', {'course': course, 'announcements': announcements})







