from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

# Create your models here.
class SoftwarePackage(models.Model):
    name = models.CharField(max_length=255)
    description = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101)  # 10 * (max_length of base_field + 1)
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Booking(models.Model):
    package = models.ForeignKey(SoftwarePackage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

