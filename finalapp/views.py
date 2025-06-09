from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from .models import Student, Enrollment
from .forms import StudentForm, EnrollmentForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(full_name__icontains=query) | Student.objects.filter(student_id__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'index.html', {'students': students, 'query': query})


def student_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    student = get_object_or_404(Student, pk=pk)
    enrollments = Enrollment.objects.filter(student=student)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = student
            enrollment.save()
            return redirect('student_detail', pk=student.id)
    else:
        form = EnrollmentForm()

    return render(request, 'student_detail.html', {
        'student': student,
        'enrollments': enrollments,
        'form': form
    })

def student_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except IntegrityError:
                form.add_error('student_id', 'This student ID already exists.')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('index')

def enrollment_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=enrollment.student.pk)
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'enrollment_form.html', {'form': form, 'enrollment': enrollment})


def enrollment_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    enrollment = get_object_or_404(Enrollment, pk=pk)
    student_pk = enrollment.student.pk
    enrollment.delete()
    return redirect('student_detail', pk=student_pk)

def add_enrollment(request, student_id):
    if not request.user.is_authenticated:
        return redirect('login')

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = student
            enrollment.save()
            return redirect('student_detail', pk=student.id)
    else:
        form = EnrollmentForm()

    return render(request, 'add_enrollment.html', {
        'form': form,
        'student': student
    })