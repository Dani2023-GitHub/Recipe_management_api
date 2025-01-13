from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICE = [
        (MALE, "Male"),
        (FEMALE, "Female")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', default='default_profile_image.jpg')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=MALE)

    def __str__(self):
        return self.user.username
