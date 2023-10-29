from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse
from datetime import datetime, timedelta
import pytz
from .models import Coach, Lesson, Feedback, Booking, Contact


class TestAdmin(TestCase):

    # instantiate user, coach, lesson, feedback, booking, and contact
    @classmethod
    def setUpTestData(self):
        # Create a superuser for admin login
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@rollercriu.com'
        )

        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email='test@email.com'
            )

        self.coach = Coach.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@rollercriu.com',
            bio='This is a test bio',
        )

        self.lesson = Lesson.objects.create(
            title='Test Lesson 1',
            slug='test-lesson-1',
            lesson_start=datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc),
            lesson_level=Lesson.BEGINNER,
            duration=timedelta(hours=1),
            location='Test Location 1',
            coach=self.coach,
            content='Test content for lesson 1',
        )

        self.feedback = Feedback.objects.create(
            lesson=self.lesson,
            username=self.user,
            email='user1@email.com',
            body='Feedback 1',
        )

        self.booking = Booking.objects.create(
            lesson=self.lesson,
            username=self.user,
            places_reserved=1,
        )

        self.contact = Contact.objects.create(
            name='Jane',
            email='jane@email.com',
            contact_message='This is a test contact message'
        )
