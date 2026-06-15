from django.urls import path
from . import views

urlpatterns = [
    path('employer/overview', views.employer_overview, name='employer overview'),
    path('employer/jobs', views.employer_jobs, name='employer jobs'),
    path('employer/applications', views.employer_applications, name='employer applications'),
    path('employer/interviews', views.employer_interviews, name='employer interviews'),
    path('employer/profile', views.employer_profile, name='employer profile'),
]