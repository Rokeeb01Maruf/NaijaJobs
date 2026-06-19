from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Employer.models import JobPost, EmployerProfile
from .models import Application

def Home(request):
    jobs = JobPost.objects.filter(is_active = True)
    companies = EmployerProfile.objects.filter(
        user__job_posts__is_active=True).values_list("company_name", flat=True).distinct()
    return render(request, "routes/home.html", {"jobs" : jobs, "companies" : companies})

def JobDetail(request, job_id):
    id = job_id
    applicant = request.user
    job = get_object_or_404(JobPost, id=id)
    if Application.objects.filter(applicant=applicant, job=job).exists():
        applied = True
    else:
        applied = False
    job = get_object_or_404(
        JobPost,
        id=job_id,
        is_active=True
    )
    return render(request, "routes/job_detail.html", {"job" : job, "applied" : applied})

@login_required
def Apply(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    if request.user.role == "Employer":
        return redirect("home")
    if Application.objects.filter(applicant = request.user, job = job).exists():
        return redirect("job_detail", job_id)
    Application.objects.create(
        applicant = request.user,
        job = job
    )
    return redirect("my_applications")

@login_required
def Logout(request):
    logout(request)
    return redirect("home")

@login_required
def Job_Applications(request):
    if(request.user.role == "Employer"):
        return redirect("home")
    job_applications = request.user.applications.all()
    total_applications = request.user.applications.all().count()
    pending = request.user.applications.all().filter(status = "pending").count()
    total_acceptance = request.user.applications.all().filter(status = "Accepted").count()
    total_rejected = request.user.applications.all().filter(status = "Rejected").count()
    return render(request, "routes/job-applications.html", {
        "applications" : job_applications,
          "total" : total_applications,
          "pending" : pending,
          "accepted" : total_acceptance,
          "rejected" : total_rejected
        })
# Create your views here.
