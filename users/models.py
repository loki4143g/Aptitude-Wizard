from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    LEVEL_CHOICES = [
        ('B', 'bronze'),
        ('S', 'silver'),
        ('G', 'gold'),
        ('P', 'platinum'),
        ('D', 'daimond'),
        ('H', 'heroic'),
        ('M', 'grand Master'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='B')
    rank = models.IntegerField(default=100000)
    image = CloudinaryField('image', null=True, blank=True)
    total_score = models.IntegerField(default=0)
    problems_solved = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name