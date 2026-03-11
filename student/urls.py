from django.urls import path
from . import views


urlpatterns = [
    path('',views.students,name="students"),
    path('add/',views.add_students, name="add_student"),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('update_student/<int:id>',views.update_student,name='update_student'),
    
]
