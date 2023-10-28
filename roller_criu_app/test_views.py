from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import pytz
from .models import Coach, Lesson, Feedback, Booking, Contact


class TestViews(TestCase):

    # instantiate coach, lesson, feedback, booking, and contact
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )

        cls.coach = Coach.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@rollercriu.com',
            bio='This is a test bio',
            specialization=Coach.RECREATIONAL,
            years_of_experience=5,
            status=1
        )

        cls.lesson = Lesson.objects.create(
            title='Test Lesson 1',
            slug='test-lesson-1',
            lesson_start=datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc),
            lesson_level=Lesson.BEGINNER,
            duration=timedelta(hours=1),
            location='Test Location 1',
            coach=cls.coach,
            content='Test content for lesson 1',
            status=0
        )

        cls.feedback = Feedback.objects.create(
            lesson=cls.lesson,
            username=cls.user,
            email='user@email.com',
            body='Feedback 2',
            approved=True
        )

        cls.booking = Booking.objects.create(
            lesson=cls.lesson,
            username=cls.user,
            places_reserved=1,
            approved='approved'
        )

        cls.contact = Contact.objects.create(
            name='Jane',
            email='jane@email.com',
            contact_message='This is a test contact message'
        )

    # get index page and check if correct templates are being used
    def test_get_lesson_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    # get about page and check if correct templates are being used
    def test_get_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about.html')

    # get contact page and check if correct templates are being used
    def test_get_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'contact.html')

    # get my bookings page and check if correct templates are being used
    def test_get_my_bookings_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'my_bookings.html')

    # get lesson detail page and check if correct templates are being used
    def test_get_lesson_detail_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about.html')

    # check if the user can toggle like and unlike
    def test_can_toggle_like_lesson(self):
        self.client.login(username='testuser', password='12345')

        lesson_detail_url = reverse('lesson_detail', kwargs={'slug': 'test-lesson-1'})
        response = self.client.get(lesson_detail_url)

        numlikes = self.lesson.number_of_likes()
        self.assertEqual(numlikes, 0)

        like_url = reverse('lesson_like', kwargs={'slug': 'test-lesson-1'})
        response = self.client.post(like_url)

        self.assertEqual(response.status_code, 302)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.number_of_likes(), 1)

        response = self.client.post(like_url)

        self.assertEqual(response.status_code, 302)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.number_of_likes(), 0)
