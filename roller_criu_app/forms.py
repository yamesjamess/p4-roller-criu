from django import forms
from .models import Feedback, Contact, Booking


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_message')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('places_reserved',)