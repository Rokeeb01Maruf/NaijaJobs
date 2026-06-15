from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL

class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )

    company_name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    location = models.TextField()
    website = models.TextField()
    about_us = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    linkedin = models.TextField()
    office_held = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.company_name} {self.phone}"

class JobPost(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_posts"
    )
    status_options = (('open', 'Open'), ('closed', 'Closed'))
    type_options = (('full_time', 'Full Time'), ('part_time', 'Part Time'), ('internship', 'Internship'), ('contract', 'Contract'))
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=type_options, db_index=True)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, db_index=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_closing = models.DateField()
    status = models.CharField(max_length=20, choices=status_options, db_index=True, default="Open")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.salary_min > self.salary_max:
            raise ValidationError("Minimum salary cannot be greater than maximum salary.")
# Create your models here.
