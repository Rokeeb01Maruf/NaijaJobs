from django.urls import path
from . import views

urlpatterns = [
    path('employer/', views.employer_view, name='employer'),
]