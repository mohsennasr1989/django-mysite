from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class CustomUser(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        ordering = ('id', 'user', 'firstname', 'lastname', 'cellphone')

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.CharField(max_length=20)
    firstname = models.CharField(verbose_name="نام", max_length=200)
    lastname = models.CharField(verbose_name="نام خانوادگی", max_length=200)
    cellphone = models.CharField(verbose_name="تلفن همراه", max_length=200)
    profile = models.ImageField(verbose_name="عکس", default='profile.jpg', upload_to='profile_images')
    create_date = models.DateTimeField(verbose_name="تاریخ ایجاد", blank=True, null=True)
    last_login_date = models.DateTimeField(verbose_name="تاریخ آخرین ورود", blank=True, null=True)
