from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalapp.urls')),
    path('', views.index, name='index'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
