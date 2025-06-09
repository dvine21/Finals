from django.contrib import admin
from django.urls import path, include
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalapp.urls')),
    path('', views.index, name='index'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),

]
