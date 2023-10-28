from django.test import TestCase
from .forms import FeedbackForm, BookingForm, ContactForm


class TestFeedbackForm(TestCase):

    # test to check whether if a feedback is provided or not
    def test_feedback_form_is_required(self):
        form_data = {'body': ''}
        form = FeedbackForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    # test to check if form is valid
    def test_feedback_form_valid(self):
        form_data = {'body': 'This is a test feedback.'}
        form = FeedbackForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # test to check if form fields are set up correctly
    def test_fields_in_form(self):
        form = FeedbackForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestContactForm(TestCase):

    # test to check whether if all the fields has been provided with data
    def test_contact_form_is_required(self):
        form_data = {
            'name': '',
            'email': '',
            'contact_message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertIn('contact_message', form.errors.keys())
        self.assertEqual(form.errors['contact_message'][0], 'This field is required.')
