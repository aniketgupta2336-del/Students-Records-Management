from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from Student_Records_Management.email_utils import send_confirmation_email   # ✅ fixed import
   # ✅ Correct import (different folder)


# 🏠 Home Page
@login_required
def home(request):
    return render(request, "home.html")


# ➕ Add Student
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()   # save student to DB

            # ✅ Send confirmation email after saving
            send_confirmation_email(
                student.name,
                student.email,    # email address to send confirmation
                student.roll_no,
                student.course,
                student.contact   # ✅ added contact number
            )

            messages.success(request, "Student added successfully ✅ (Email sent 📧)")
            return redirect("view_student")
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})


# 👀 View Student List
@login_required
def view_student(request):
    students = Student.objects.all()
    return render(request, "view_student.html", {"students": students})


# ✏️ Edit Student
@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully ✨")
            return redirect("view_student")
    else:
        form = StudentForm(instance=student)

    return render(request, "edit.html", {"form": form})


# ❌ Delete Student
@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully ❌")
    return redirect("view_student")


# 🔑 User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password ❌")

    return render(request, "login.html")


# 🚪 User Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")
