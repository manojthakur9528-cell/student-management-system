from django.shortcuts import render
from .models import Student
# Create your views here.

def students(request):
    student_data =Student.objects.all()
    print(student_data)

    data = {
        'student_data': student_data,
    }
    return render(request,'student/students.html',data)     


def add_students(request):

    if request.method =='POST':
        student_name = request.POST.get('input_name')
        student_email = request.POST.get('input_email')
        student_phone = request.POST.get('input_phone')
        

        Student.objects.create(
            name = student_name,
            email = student_email,
            phone = student_phone,
    )
    return render(request,'student/add_students.html')
