from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    birthday = models.DateField()
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    section = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activity_grade = models.FloatField()
    quiz_grade = models.FloatField()
    exam_grade = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.subject}"
