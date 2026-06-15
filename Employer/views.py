from django.shortcuts import render, redirect
from .models import EmployerProfile, JobPost
from django.contrib.auth.decorators import login_required

@login_required
def employer_overview(request):
    user = request.user
    if user.role != "Employer":
        return redirect("home")
    my_jobs = user.job_posts.all()
    company = user.employer_profile
    return render(request, 
                  'employer/routes/overview.html', 
                  {"jobs" : my_jobs, 
                   "employer" : company, 
                   "job_counts" : my_jobs.count(),
                   "active_jobs" : my_jobs.filter(is_active=True).count()})

@login_required
def employer_jobs(request):
    user = request.user
    if user.role != "Employer":
        return redirect("home")
    company = user.employer_profile
    my_jobs = user.job_posts.all()
    return render(request, 'employer/routes/jobs.html', {
        "employer" : company,
        "jobs" : my_jobs
    })

@login_required
def employer_applications(request):
    if request.user.role != "Employer":
        return redirect("home")
    return render(request, 'employer/routes/applications.html')

@login_required
def employer_interviews(request):
    if request.user.role != "Employer":
        return redirect("home")
    return render(request, 'employer/routes/interviews.html')

@login_required
def employer_profile(request):
    user = request.user

    if user.role != "Employer":
        return redirect("home")

    if request.method == "GET":
        try:
            profile = user.employer_profile
            return render(request, "employer/routes/profile.html", {
                "not_found": False,
                "profile": profile
            })

        except EmployerProfile.DoesNotExist:
            return render(request, "employer/routes/profile.html", {
                "not_found": True
            })

    elif request.method == "POST":
        if user.role != "Employer":
            return redirect("home")

        name = request.POST.get("name")
        industry = request.POST.get("industry")
        location = request.POST.get("location")
        website = request.POST.get("website")
        about = request.POST.get("about-us")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        linkedin = request.POST.get("linkedin")
        office = request.POST.get("office")

        # simple validation
        if not all([name, industry, location, website, about, email, phone, linkedin, office]):
            return render(request, "employer/routes/profile.html", {
                "not_found": True,
                "error": "Invalid input"
            })

        if not website.startswith("https://"):
            return render(request, "employer/routes/profile.html", {
                "error": "Invalid website"
            })

        if not linkedin.startswith("https://"):
            return render(request, "employer/routes/profile.html", {
                "error": "Invalid linkedin"
            })

        if not phone.startswith("0"):
            return render(request, "employer/routes/profile.html", {
                "error": "Invalid phone number"
            })

        profile = EmployerProfile.objects.create(
            user=user,
            company_name=name,
            industry=industry,
            location=location,
            website=website,
            about_us=about,
            email=email,
            phone=phone,
            linkedin=linkedin,
            office_held=office
        )

        return redirect("employer profile")
# Create your views here.
