from django import forms
from .models import Feedback, Contact, Booking


class FeedbackForm(forms.ModelForm):
    """
    A form for creating or updating feedback instances.

    Attributes:
        Meta (class):
            model (class): The model class associated with this form (Feedback)
            fields (tuple): The fields from the model to include in the form.
    """

    class Meta:
        model = Feedback
        fields = ('body',)


class ContactForm(forms.ModelForm):
    """
    A form for creating or updating contact instances.

    Attributes:
        Meta (class):
            model (class): The model class associated with this form (Contact).
            fields (tuple): The fields from the model to include in the form.
    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_message')


class BookingForm(forms.ModelForm):
    """
    A form for creating or updating booking instances.

    Attributes:
        Meta (class):
            model (class): The model class associated with this form (Booking).
            fields (tuple): The fields from the model to include in the form.
    """

    class Meta:
        model = Booking
        fields = ('places_reserved',)
