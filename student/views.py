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

        Student.objects.create(      # ✅ pehle create karo
            name=student_name,
            email=student_email,
            phone=student_phone,
        )
        return redirect("students")  # ✅ phir redirect karo
    return render(request, 'student/add_students.html')

def delete_student(request, id):
    my_student = Student.objects.get(id=id)
    my_student.delete()
    return redirect('students')

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get('input_name')    # ✅ input_name
        student.email = request.POST.get('input_email')  # ✅ input_email
        student.phone = request.POST.get('input_phone')  # ✅ phone (not phone_number)
        student.save()             # ✅ uncomment kiya
        return redirect('students') # ✅ uncomment kiya
    parameters = {"student": student}
    return render(request, "student/update_student.html", parameters)