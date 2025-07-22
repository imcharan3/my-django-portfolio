from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal_details/', views.personal_details, name='personal_details'),
     path('education/', views.education_view, name='education'),
     path('personal_skills/', views.personal_skills_view, name='personal_skills'),
     path('personal_projects/', views.personal_projects_view, name='personal_projects'),
     path('internships/', views.internships_view, name='internships'),
]
