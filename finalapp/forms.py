from django import forms
from .models import Student, Enrollment, Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'student_id',
            'email',
            'birthday',
            'course',
            'year',
            'section',
            'phone_number',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

class EnrollmentForm(forms.ModelForm):
    subject_name = forms.CharField(label='Subject')  # Custom input instead of dropdown

    class Meta:
        model = Enrollment
        fields = ['subject_name', 'activity_grade', 'quiz_grade', 'exam_grade']

    def save(self, commit=True):
        subject_name = self.cleaned_data.pop('subject_name')
        subject, created = Subject.objects.get_or_create(name=subject_name)
        enrollment = super().save(commit=False)
        enrollment.subject = subject
        if commit:
            enrollment.save()
        return enrollment

def clean_student_id(self):
    student_id = self.cleaned_data['student_id']
    if Student.objects.filter(student_id=student_id).exists():
        raise forms.ValidationError("Student ID already exists.")
    return student_id        
