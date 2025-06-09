from django.urls import path
from . import views
from .forms import CustomLoginForm


urlpatterns = [
    path('', views.index, name='index'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('enrollment/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollment/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    path('student/<int:student_id>/add-enrollment/', views.add_enrollment, name='add_enrollment'),
]
