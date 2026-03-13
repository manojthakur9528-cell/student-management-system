from django.shortcuts import render, redirect
from .models import Student

def students(request):
    student_data = Student.objects.all()
    data = {'student_data': student_data}
    return render(request, 'student/students.html', data)

def add_students(request):
    if request.method == 'POST':
        student_name = request.POST.get('input_name')
        student_email = request.POST.get('input_email')
        student_phone = request.POST.get('input_phone')
        student_image = request.FILES.get('input_photo')

        Student.objects.create(
            name=student_name,
            email=student_email,
            phone=student_phone,
            image=student_image,
        )
        return redirect("students")
    return render(request, 'student/add_students.html')

def delete_student(request, id):
    my_student = Student.objects.get(id=id)
    my_student.delete()
    return redirect('students')

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get('input_name')
        student.email = request.POST.get('input_email')
        student.phone = request.POST.get('input_phone')
        student_image = request.FILES.get('input_photo')
        if student_image:                  # ✅ FIX — image save ho rahi hai ab
            student.image = student_image
        student.save()
        return redirect('students')
    parameters = {"student": student}
    return render(request, "student/update_student.html", parameters)