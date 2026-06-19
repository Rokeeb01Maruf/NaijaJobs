from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("logout", views.Logout, name="logout"),
    path("my-application", views.Job_Applications, name="my_applications"),
    path("job/<int:job_id>/", views.JobDetail, name="job_detail"),
    path("apply/job/<int:job_id>/", views.Apply, name="apply"),
]