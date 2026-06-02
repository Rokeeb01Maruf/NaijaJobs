import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role_options = (('Employer', 'employer'),('seeker', 'Job seeker'))
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    role = models.CharField(max_length=20, choices= role_options)

# Create your models here.
