from django.db import models


# Create your models here.

class User(models.Model):

    def __str__(self):
        return self.user_name

    user_id = models.CharField(max_length=20)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile = models.CharField(max_length=500,  default="https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png")
    create_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)




