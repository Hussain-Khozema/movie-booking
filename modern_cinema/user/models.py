from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^[8-9]\d{7}$', message="Phone number must be of 8 digits")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=8, null=True)

    def __str__(self):
        return self.user.username
