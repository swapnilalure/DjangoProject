from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)
    otp = models.IntegerField(null=True, blank=True)
    login_type = models.CharField(max_length=55, null=True, blank=True)
    unique_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="+")
    created_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="+")
    modified_on = models.DateTimeField(null=True)
    timezone = models.CharField(max_length=125, null=True, blank=True)
    browser_agent = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="+")
    deleted_on = models.DateTimeField(null=True)

    # username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()
