from django.urls import path
from .views import AttendanceAPI

urlpatterns = [
    path('', AttendanceAPI.as_view(), name='attendance'),
]
