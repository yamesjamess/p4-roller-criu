from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Coach(models.Model):
    RECREATIONAL = 'recreational'
    FREESTYLE = 'freestyle'
    DANCE = 'dance'
    PAIRS = 'pairs'

    SPECIALIZATION_CHOICES = [
        (RECREATIONAL, 'Recreational'),
        (FREESTYLE, 'Freestyle'),
        (DANCE, 'Dance'),
        (PAIRS, 'Pairs'),
    ]

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=140, help_text="Enter a brief bio")
    image = CloudinaryField('image', default='placeholder')
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES, default=RECREATIONAL)
    years_of_experience = models.PositiveIntegerField(default='1', help_text="Enter a positive integer.")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'Coach {self.first_name} {self.last_name}'


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
    # duration = models.DurationField()
    location = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='lesson_likes', blank=True)
    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING, related_name='lesson_coach')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lesson_time']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Feedback(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='feedbacks')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feedbacks')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Feedback {self.body} by {self.username}'


class Booking(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_bookings')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.lesson} is booked by {self.username}'
