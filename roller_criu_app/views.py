from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Lesson, Coach, Feedback, Contact, Booking
from .forms import FeedbackForm, ContactForm, BookingForm


class LessonList(generic.ListView):
    """
    View for displaying a list of lessons.

    Attributes:
        model (class): The model to retrieve data from (Lesson).
        queryset (QuerySet): The filtered queryset of lessons.
        template_name (str): The name of the template to render.
        paginate_by (int): The number of lessons to display per page.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view.
    """

    model = Lesson
    queryset = Lesson.objects.filter(status=1).order_by("lesson_start")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = \
            'Learn to become an artistic roller skater with us'
        return context


class About(generic.ListView):
    """
    View for displaying information about coaches.

    Attributes:
        model (class): The model to retrieve data from (Coach).
        queryset (QuerySet): The filtered queryset of coaches.
        template_name (str): The name of the template to render.
        paginate_by (int): The number of coaches to display per page.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view.
    """

    model = Coach
    queryset = Coach.objects.filter(status=1).order_by("first_name")
    template_name = "about.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "About"
        return context


class Contact(CreateView):
    """
    View for handling contact messages.

    Attributes:
        model (class): The model to create (Contact).
        form_class (class): The form class for contact messages (ContactForm).
        template_name (str): The name of the template to render.
        success_url (str): The URL to redirect to upon successful form
            submission.

    Methods:
        get_context_data(**kwargs): Adds additional context data to the view.
    """

    model = Contact
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("contact_success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Contact"
        return context


class LessonDetail(View):
    """
    View for displaying details about a lesson.

    Methods:
        get(request, slug, *args, **kwargs): Handles GET requests for lesson
            details.
        post(request, slug, *args, **kwargs): Handles POST requests for lesson
            details.
        user_has_booked(user, lesson): Checks if the user has already booked
            the lesson.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        coach = lesson.coach
        feedbacks = lesson.feedbacks.filter(
            approved=True).order_by("-created_on")
        user = get_user(request)
        has_booking = False
        liked = False

        booking_form = BookingForm()

        if user.is_authenticated:
            has_booking = self.user_has_booked(user, lesson)

        if lesson.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "lesson_detail.html",
            {
                "lesson": lesson,
                "feedbacks": feedbacks,
                "coach": coach,
                "submitted_feedback": False,
                "liked": liked,
                "has_booking": has_booking,
                "feedback_form": FeedbackForm(),
                "booking_form": booking_form,
                "page_title": lesson.title,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        coach = lesson.coach
        feedbacks = lesson.feedbacks.filter(
            approved=True).order_by("-created_on")
        liked = False
        booking_form = BookingForm()
        user = get_user(request)
        submitted_feedback = False
        submitted_booking = False

        if lesson.likes.filter(id=self.request.user.id).exists():
            liked = True

        if user.is_authenticated:
            if "feedback_submit" in request.POST:
                feedback_form = FeedbackForm(data=request.POST)
                if feedback_form.is_valid():
                    feedback_form.instance.email = request.user.email
                    feedback_form.instance.name = request.user.username
                    feedback_form.instance.username_id = request.user.id
                    feedback = feedback_form.save(commit=False)
                    feedback.lesson = lesson
                    feedback.save()
                    submitted_feedback = True
                else:
                    feedback_form = FeedbackForm()

            has_booking = self.user_has_booked(user, lesson)
            if has_booking:
                # User has already made a booking, return an error response
                messages.error(
                    request,
                    "You have already booked this lesson!"
                    "Please check My Bookings page.",
                )
            else:
                if "booking_submit" in request.POST:
                    booking_form = BookingForm(data=request.POST)
                    if booking_form.is_valid():
                        booking = booking_form.save(commit=False)
                        booking.lesson = lesson
                        booking.username = request.user
                        booking.save()
                        submitted_booking = True
                        messages.success(
                            request, "Thank you for your booking request!")
                    else:
                        booking_form = BookingForm()

        return render(
            request,
            "lesson_detail.html",
            {
                "lesson": lesson,
                "feedbacks": feedbacks,
                "coach": coach,
                "submitted_feedback": submitted_feedback,
                "submitted_booking": submitted_booking,
                "liked": liked,
                "feedback_form": FeedbackForm(),
                "booking_form": booking_form,
                "page_title": lesson.title,
            },
        )

    def user_has_booked(self, user, lesson):
        return Booking.objects.filter(lesson=lesson, username=user).exists()


class LessonLike(LoginRequiredMixin, View):
    """
    View for handling lesson likes.

    Methods:
        post(request, slug, *args, **kwargs): Handles POST requests
            for liking/unliking lessons.
    """

    def post(self, request, slug, *args, **kwargs):
        lesson = get_object_or_404(Lesson, slug=slug)

        if lesson.likes.filter(id=request.user.id).exists():
            lesson.likes.remove(request.user)
        else:
            lesson.likes.add(request.user)

        return HttpResponseRedirect(reverse("lesson_detail", args=[slug]))


class MyBookings(LoginRequiredMixin, View):
    """
    View for managing user bookings.

    Methods:
        get(request, *args, **kwargs): Handles GET requests for user bookings.
        post(request, *args, **kwargs): Handles POST requests for canceling
            user bookings.
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        current_time = timezone.now()

        future_bookings = Booking.objects.filter(
            username=user, lesson__lesson_start__gt=current_time
        ).order_by("lesson__lesson_start")
        past_bookings = Booking.objects.filter(
            username=user, lesson__lesson_start__lte=current_time
        ).order_by("-lesson__lesson_start")
        return render(
            request,
            "my_bookings.html",
            {
                "future_bookings": future_bookings,
                "past_bookings": past_bookings,
                "page_title": "My Bookings",
            },
        )

    def post(self, request, *args, **kwargs):
        booking_id = request.POST.get("booking_id")
        if booking_id:
            # Find the booking with the provided ID
            booking = Booking.objects.filter(id=booking_id).first()

            if booking and booking.username == request.user:
                # Cancel the booking
                booking.delete()
                messages.success(request, "Booking canceled successfully.")
            else:
                messages.error(request, "Unable to cancel the booking.")

        return HttpResponseRedirect(reverse("my_bookings"))
