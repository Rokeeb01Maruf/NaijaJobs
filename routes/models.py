from django.db import models
from django.conf import settings
from Employer.models import JobPost
User = settings.AUTH_USER_MODEL

class Application(models.Model):
    STATUS_CHOICES = (('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'))
    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        JobPost,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("applicant", "job")
    
    def __str__(self):
        return f"{self.applicant} applied for {self.job}"
# Create your models here.
