from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.students),
    path('addstd/',views.add_students),
    
]
