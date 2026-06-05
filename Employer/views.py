from django.shortcuts import render


def employer_view(request):
    return render(request, 'employer/dashboard.html')
# Create your views here.
