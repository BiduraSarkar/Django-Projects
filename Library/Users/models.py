from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #one to one relationship between User and Profile
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #CASCADE => If user is deleted then profile is deleted too
    address = models.CharField(max_length=225)
    image = models.ImageField(default = 'profilepic.jpg',upload_to = 'profile_pictures')

    def __str__(self):
        return self.user.username
