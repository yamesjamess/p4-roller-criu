from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
import pytz
from .models import Coach, Lesson, Feedback, Booking, Contact


class TestModels(TestCase):

    # instantiate user, coach, lesson, feedback, booking, and contact
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

    # test the __str__ method for Coach
    def test_coach_str(self):
        self.assertEqual(
            str(self.coach),
            f'Coach {self.coach.first_name} {self.coach.last_name}')

    # test the __str__ method for Lesson
    def test_lesson_str(self):
        self.assertEqual(str(self.lesson), self.lesson.title)

    # test the __str__ method for Feedback
    def test_feedback_str(self):
        self.assertEqual(
            str(self.feedback),
            f'Feedback {self.feedback.body} by {self.user.username}')

    # test the __str__ method for Booking
    def test_booking_str(self):
        self.assertEqual(
            str(self.booking),
            f'{self.booking.lesson} is booked by {self.user.username}')

    # test the __str__ method for Contact
    def test_contact_str(self):
        self.assertEqual(str(
            self.contact),
            f'Contact message submitted by {self.contact.name} on {self.contact.created_on}')

    # test default values in Coach
    def test_coach_default_values(self):
        self.assertEqual(self.coach.image, 'placeholder')
        self.assertEqual(self.coach.specialization, 'recreational')
        self.assertEqual(self.coach.years_of_experience, 1)
        self.assertEqual(self.coach.status, 0)

    # test years of experience is a positive integer in Coach
    def test_coach__yoe_is_positive_integer(self):
        self.assertTrue(self.coach.years_of_experience >= 0)
        self.assertFalse(self.coach.years_of_experience <= 0)

    # test number of likes in Lesson
    def test_lesson_number_of_likes(self):
        self.assertEqual(self.lesson.number_of_likes(), 0)

    # test default values in Lesson
    def test_lesson_default_level(self):
        self.assertEqual(self.lesson.lesson_level, 'beginner')
        self.assertEqual(self.lesson.status, 0)
        self.assertEqual(self.lesson.featured_image, 'placeholder')
        self.assertEqual(self.lesson.duration, timedelta(hours=1))

    # test ordering in Feedback
    def test_feedback_ordering(self):
        feedback2 = Feedback.objects.create(
            lesson=self.lesson,
            username=self.user,
            email='user2@email.com',
            body='Feedback 2',
            approved=True
        )

        feedbacks = Feedback.objects.all()

        self.assertEqual(feedbacks[0], self.feedback)
        self.assertEqual(feedbacks[1], feedback2)

    # test default values in Feedback
    def test_feedback_default_values(self):
        self.assertEqual(self.feedback.approved, False)

        current_datetime = timezone.now()
        tolerance = timezone.timedelta(seconds=1)
        self.assertLessEqual(
            abs(self.feedback.created_on - current_datetime), tolerance)

    # test default values in Booking
    def test_booking_default_values(self):
        self.assertEqual(self.booking.approved, 'pending')

    # test place reserved value is not less than 1 in Booking
    def test_places_reserved_no_less_than_one(self):
        self.assertTrue(self.booking.places_reserved >= 1)

    # test default values in Contact
    def test_contact_default_values(self):
        current_datetime = timezone.now()
        tolerance = timezone.timedelta(seconds=1)
        self.assertLessEqual(
            abs(self.contact.created_on - current_datetime), tolerance)
