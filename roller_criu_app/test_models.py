from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import pytz
from .models import Coach, Lesson, Feedback, Booking, Contact


class TestModels(TestCase):

    # instantiate coach, lesson, feedback, booking, and contact
    @classmethod
    def setUpTestData(self):
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
            specialization=Coach.RECREATIONAL,
            years_of_experience=5,
            status=1
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
            status=0
        )

        self.feedback = Feedback.objects.create(
            lesson=self.lesson,
            username=self.user,
            email='user@email.com',
            body='Feedback 2',
            approved=True
        )

        self.booking = Booking.objects.create(
            lesson=self.lesson,
            username=self.user,
            places_reserved=1,
            approved='approved'
        )

        self.contact = Contact.objects.create(
            name='Jane',
            email='jane@email.com',
            contact_message='This is a test contact message'
        )

    # test the __str__ method for Coach
    def test_coach_str(self):
        self.assertEqual(str(self.coach), f'Coach {self.coach.first_name} {self.coach.last_name}')

    # test the __str__ method for Lesson
    def test_lesson_str(self):
        self.assertEqual(str(self.lesson), self.lesson.title)

    # test the __str__ method for Feedback
    def test_feedback_str(self):
        self.assertEqual(str(self.feedback), f'Feedback {self.feedback.body} by {self.user.username}')

    # test the __str__ method for Booking
    def test_booking_str(self):
        self.assertEqual(str(self.booking), f'{self.booking.lesson} is booked by {self.user.username}')

    # test the __str__ method for Contact
    def test_contact_str(self):
        self.assertEqual(str(self.contact), f'Contact message submitted by {self.contact.name} on {self.contact.created_on}')