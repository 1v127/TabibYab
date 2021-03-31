from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from creator import views

app_name = 'creator'

urlpatterns = [
  #  path('', views.CreateDoctor.as_view(), name='create_doctor'),
    path('<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('educations/<int:doctor_id>/', views.create_doctor_education, name='create_doctor_educations'),
    path('skills/<int:doctor_id>/', views.create_doctor_skill, name='create_doctor_skills'),
    path('experiences/<int:doctor_id>/', views.create_doctor_experience, name='create_doctor_experiences'),

    path('registration/login/', auth_views.LoginView.as_view(), name='login'),
    path('registration/logout/', views.logout_view, name='logout'),
    path('registration/register/', views.register_view, name='register'),
    path('registration/profile/', views.view_profile, name='profile'),
    path('registration/edit-profile/', views.edit_profile, name='edit_profile'),
    path('registration/password/', views.change_password, name='change_password'),
   # path('post-creator/', views.post_creator)
    path('', views.post_creator, name='create_doctor')
]
