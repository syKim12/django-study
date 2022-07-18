from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    #여기서 null, blank는 false로 바꿔야함
    phone = PhoneNumberField(unique = True, null = True, blank = True)

    def __str__(self):
        return self.email
