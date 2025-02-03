from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class Category(models.Model):
    section = models.CharField(max_length=255, default="Quantitative Aptitude")
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Question(models.Model):

    OPTION_CHOICES = [
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    ]
    TAG_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
        ('D', 'Daimond'),
        ('H', 'Heroic'),
        ('M', 'Grand Master'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=OPTION_CHOICES)
    explanation = models.TextField(blank=True, null=True)
    solution_image = CloudinaryField("image", null=True, blank=True)
    tag = models.CharField(choices=TAG_CHOICES, max_length=1)

    def __str__(self):
        return self.category.name