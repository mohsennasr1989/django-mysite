from django.db import models


# Create your models here.

class User(models.Model):

    def __str__(self):
        return self.user_name

    user_id = models.CharField(max_length=20)
    user_first_name = models.CharField(max_length=200)
    user_last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_cellphone = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_profile_image = models.FileField(blank=True)
    user_create_date = models.DateTimeField(blank=True)
    user_last_login_date = models.DateTimeField(blank=True)




