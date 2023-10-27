from django.test import TestCase
from .forms import FeedbackForm, BookingForm, ContactForm


class TestFeedbackForm(TestCase):

    # test to check whether if a feedback is provided or not
    def test_feedback_form_is_required(self):
        form = FeedbackForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
    
