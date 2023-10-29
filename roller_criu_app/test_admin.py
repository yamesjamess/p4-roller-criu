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

    # test to check if admin can login and get to Coach database page
    def test_coach_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin:roller_criu_app_coach_changelist'))
        self.assertEqual(response.status_code, 200)

    # test to check if admin can login and get to Lesson database
    def test_lesson_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin:roller_criu_app_lesson_changelist'))
        self.assertEqual(response.status_code, 200)

    # test to check if admin can login and get to feedback database page
    def test_feedback_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin:roller_criu_app_feedback_changelist'))
        self.assertEqual(response.status_code, 200)

    # test to check if admin can login and get to booking database page
    def test_booking_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin:roller_criu_app_booking_changelist'))
        self.assertEqual(response.status_code, 200)

    # test to check if admin can login and get to Contact database page
    def test_contact_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin:roller_criu_app_contact_changelist'))
        self.assertEqual(response.status_code, 200)

    # Check if admin user can approve feedback
    def test_admin_approve_feedback(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('admin:roller_criu_app_feedback_changelist'),
            {
                'action': 'approved_feedback',
                '_selected_action': [self.feedback.id],
            }
        )
        self.assertEqual(response.status_code, 302)
        self.feedback.refresh_from_db()
        self.assertTrue(self.feedback.approved)

    # Check if admin user can unapprove feedback
    def test_admin_unapprove_feedback(self):
        # Create a test feedback with approved set to True
        feedback = Feedback.objects.create(
            lesson=self.lesson,
            username=self.user,
            email='user1@email.com',
            body='Feedback 1',
            approved=True
        )

        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('admin:roller_criu_app_feedback_changelist'),
            {
                'action': 'unapproved_feedback',
                '_selected_action': [(feedback.id)],
            }
        )
        self.assertEqual(response.status_code, 302)
        feedback.refresh_from_db()
        self.assertTrue(feedback.approved)

    # Check if admin user can approve booking
    def test_admin_approve_booking(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('admin:roller_criu_app_booking_changelist'),
            {
                'action': 'approved_booking',
                '_selected_action': [self.booking.id],
            }
        )
        self.assertEqual(response.status_code, 302)
        self.booking.refresh_from_db()
        self.assertTrue(self.booking.approved)
    
    # Check if admin user can unapprove booking
    def test_admin_unapprove_booking(self):
        # Create a test booking with approved set to approved
        booking = Booking.objects.create(
            lesson=self.lesson,
            username=self.user,
            places_reserved=1,
            approved='approved'
        )

        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            reverse('admin:roller_criu_app_booking_changelist'),
            {
                'action': 'unapproved_booking',
                '_selected_action': [(booking.id)],
            }
        )
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertTrue(booking.approved)