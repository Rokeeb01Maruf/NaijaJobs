from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import EmployerProfile, JobPost
from django.contrib.auth.decorators import login_required
from routes.models import Application
from accounts.models import User

@login_required
def employer_overview(request):
    user = request.user
    try:
        company = user.employer_profile
    except:
        company = None
    my_jobs = user.job_posts.all()
    applicants = Application.objects.filter(job__user = user).count()
    if user.role != "Employer":
        return redirect("home")
    if request.method == "GET":
        return render(request, 
                'employer/routes/overview.html', 
                {"jobs" : my_jobs, 
                "employer" : company, 
                "job_counts" : my_jobs.count(),
                "active_jobs" : my_jobs.filter(is_active=True).count(),
                "total_applicants" : applicants,
                "applications" : "empty"})
    elif request.method == "POST":
        job_id = request.POST.get("hidden")
        job = get_object_or_404(JobPost, id=int(job_id))
        applications = Application.objects.filter(job = job).all()
        return render(request, 
                'employer/routes/overview.html', 
                {"jobs" : my_jobs, 
                "employer" : company, 
                "job_counts" : my_jobs.count(),
                "active_jobs" : my_jobs.filter(is_active=True).count(),
                "total_applicants" : applicants,
                "applications" : applications})

    
    return render(request, 
                  'employer/routes/overview.html', 
                  {"jobs" : my_jobs, 
                   "employer" : company, 
                   "job_counts" : my_jobs.count(),
                   "active_jobs" : my_jobs.filter(is_active=True).count(),
                   "total_applicants" : applicants})

@login_required
def employer_jobs(request):
    user = request.user
    if user.role != "Employer":
        return redirect("home")
    if request.method == "GET":
        try:
            company = user.employer_profile
        except:
            company = None
        my_jobs = user.job_posts.all()
        return render(request, 'employer/routes/jobs.html', {
            "employer" : company,
            "jobs" : my_jobs
        })
    elif request.method == "POST":
        title = request.POST.get("title")
        job_type = request.POST.get("job_type")
        min_salary = request.POST.get("min_salary")
        max_salary = request.POST.get("max_salary")
        description = request.POST.get("description")
        category = request.POST.get("category")
        date_closing = request.POST.get("date_closing")

        if not any([title, job_type, min_salary, max_salary, description, category, date_closing]):
            return render(request, 'employer/routes/jobs.html', {"error" : "All fields are required"})
        elif max_salary < min_salary:
            return render(request, "employer/routes/jobs.html", {"error" : "Salary(max) must be larger than salary(min)"})
        else:
            post_job = JobPost.objects.create(
                user = user,
                title = title,
                job_type = job_type,
                salary_min = min_salary,
                salary_max = max_salary,
                description = description,
                category = category,
                date_closing = date_closing,
            )
            return redirect("employer jobs")

@login_required
def employer_applications(request):
    if request.user.role != "Employer":
        return redirect("home")
    employer = request.user
    try:
        registered = employer.employer_profile
        if registered:
            company = True
        else:
            company = False
    except:
        company = False
    try: 
        applied_jobs = []
        jobs = get_list_or_404(JobPost, user=employer)
        for job in jobs:
            applications = Application.objects.filter(job=job).all()
            if applications: 
                applied_jobs.append(applications)
    except:
        applied_jobs = None
    return render(request, 'employer/routes/applications.html',
                   {"applications": applied_jobs, "registered" : company})

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
@login_required   
def close_job(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(
            JobPost,
            id=job_id,
            user=request.user
        )
        job.status = "Closed"
        job.save()
    return redirect("employer jobs")

@login_required
def alter_application(request, job_id, username):
    user = request.user
    if user.role != "Employer":
        return redirect("home")
    alter = request.GET.get("alter")
    applicants = User.objects.get(username=username)
    job = get_object_or_404(JobPost, id=job_id)
    application = Application.objects.filter(applicant=applicants, job=job).first()
    if alter == "accept":
        application.status = "Accepted"
    elif alter == "reject":
        application.status = "Rejected"
    application.save()
    print(application.status)
    return redirect("employer applications")
# Create your views here.
