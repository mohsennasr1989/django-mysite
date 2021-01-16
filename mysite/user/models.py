from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class CustomUser(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.CharField(max_length=20)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    profile = models.ImageField(default='profile.jpg', upload_to='profile_images')
    create_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
