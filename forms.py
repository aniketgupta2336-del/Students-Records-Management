from django import forms
from .models import Student   # ✅ import model, don't redefine it

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll_no", "email", "course", "contact"]
