from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileMOdel(models.Model):
    profileUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='profile_user')
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    linkedIn = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=200)

