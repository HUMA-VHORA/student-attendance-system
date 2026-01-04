from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Student Attendance System API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>/admin/</li>
        <li>/students/</li>
        <li>/attendance/</li>
    </ul>
    """)

urlpatterns = [
    path('', home),                 # 👈 ROOT URL FIXED
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('attendance/', include('attendance.urls')),
]

