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
    
    # test to check if form fields are set up correctly
    def test_fields_in_form(self):
        form = FeedbackForm()
        self.assertEqual(form.Meta.fields, ('body',))
