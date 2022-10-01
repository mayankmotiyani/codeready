from django.db import models
from django.contrib.auth.models import AbstractUser
from user_application.manager import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_("email"),max_length=30,unique=True,blank=True,null=True)
    username = models.CharField(_("username"),max_length=30,blank=True)
    first_name = models.CharField(_("first name"),max_length=30,blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects =  UserManager()
