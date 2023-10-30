from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Coach(models.Model):
    """
    Model representing a coach.

    Attributes:
        first_name (CharField): The first name of the coach.
        last_name (CharField): The last name of the coach.
        email (EmailField): The email address of the coach.
        bio (CharField): A brief bio of the coach.
        image (CloudinaryField): An image representing the coach.
        specialization (CharField): The specialization of the coach (choices defined).
        years_of_experience (PositiveIntegerField): Years of coaching experience.
        status (IntegerField): The status of the coach (0 for Draft, 1 for Published).

    Meta:
        ordering (list): The default sorting order for coaches.
        verbose_name_plural (str): The plural name for this model in the admin panel.

    Methods:
        __str__(): Returns a string representation of the coach.
    """
    
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
    image = CloudinaryField('image', default='placeholder',
                            help_text="Image must be a square")
    specialization = models.CharField(
        max_length=20, choices=SPECIALIZATION_CHOICES, default=RECREATIONAL)
    years_of_experience = models.PositiveIntegerField(
        default=1, help_text="Enter a positive integer.")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['pk']
        verbose_name_plural = 'Coaches'

    def __str__(self):
        return f'Coach {self.first_name} {self.last_name}'


class Lesson(models.Model):
    """
    Model representing a lesson.

    Attributes:
        title (CharField): The title of the lesson (unique).
        slug (SlugField): A slug for the lesson (unique).
        lesson_start (DateTimeField): The date and time the lesson starts.
        lesson_level (CharField): The level of the lesson (choices defined).
        duration (DurationField): The duration of the lesson.
        location (CharField): The location of the lesson.
        coach (ForeignKey): The coach associated with the lesson.
        content (TextField): Description of the lesson.
        featured_image (CloudinaryField): An image representing the lesson.
        status (IntegerField): The status of the lesson (0 for Draft, 1 for Published).
        likes (ManyToManyField): Users who have liked the lesson.
        created_on (DateTimeField): The date and time the lesson was created.
        updated_on (DateTimeField): The date and time the lesson was last updated.

    Meta:
        ordering (list): The default sorting order for lessons.

    Methods:
        __str__(): Returns the title of the lesson.
        number_of_likes(): Returns the number of likes for the lesson.

    """

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
    lesson_start = models.DateTimeField(
        help_text="Date: YYYY-MM-DD Time: HH:MM:SS")
    lesson_level = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, default=BEGINNER)
    duration = models.DurationField(
        help_text="Format HH:MM:SS", default='01:00:00')
    location = models.CharField(max_length=100)
    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, related_name='lesson_coach')
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='lesson_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lesson_start']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Feedback(models.Model):
    """
    Model representing feedback for a lesson.

    Attributes:
        lesson (ForeignKey): The lesson associated with the feedback.
        username (ForeignKey): The user providing the feedback.
        email (EmailField): The email address of the user.
        body (TextField): The content of the feedback.
        created_on (DateTimeField): The date and time the feedback was created.
        approved (BooleanField): Whether the feedback is approved or not.

    Meta:
        ordering (list): The default sorting order for feedback.

    Methods:
        __str__(): Returns a string representation of the feedback.
    """
    
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='feedbacks')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_feedbacks')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Feedback {self.body} by {self.username}'


class Booking(models.Model):
    """
    Model representing a booking for a lesson.

    Attributes:
        lesson (ForeignKey): The lesson being booked.
        username (ForeignKey): The user making the booking.
        places_reserved (IntegerField): The number of places reserved.
        approved (CharField): The approval status of the booking (choices defined).

    Methods:
        __str__(): Returns a string representation of the booking.
    """

    APPROVAL_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('not_approved', 'Not Approved'),
    )

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='lesson_bookings')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_bookings')
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.CharField(
        max_length=12, choices=APPROVAL_CHOICES, default='pending')

    def __str__(self):
        return f'{self.lesson} is booked by {self.username}'


class Contact(models.Model):
    """
    Model representing contact messages.

    Attributes:
        name (CharField): The name of the person sending the message.
        email (EmailField): The email address of the person.
        contact_message (TextField): The content of the contact message.
        created_on (DateTimeField): The date and time the message was created.

    Meta:
        ordering (list): The default sorting order for contact messages.
        verbose_name_plural (str): The plural name for this model in the admin panel.

    Methods:
        __str__(): Returns a string representation of the contact message.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Contact message submitted by {self.name} on {self.created_on}'
