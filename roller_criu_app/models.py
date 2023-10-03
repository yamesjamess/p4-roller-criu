from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Lesson(models.Model):
    # code from https://adamj.eu/tech/2020/01/27/moving-to-django-3-field-choices-enumeration-types/
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    lesson_time = models.DateTimeField()
    lesson_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default=BEGINNER)
    location = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='lesson_likes', blank=True)
    # coach = models.ForeignKey(Coach, on_delete=models.SET_DEFAULT, default=1, related_name='lesson_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lesson_level']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Feedback(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='feedbacks')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
