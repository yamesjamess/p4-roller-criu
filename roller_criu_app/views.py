from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Lesson, Coach, Feedback, Contact, Booking
from .forms import FeedbackForm, ContactForm, BookingForm


class LessonList(generic.ListView):
    model = Lesson
    queryset = Lesson.objects.filter(status=1).order_by('lesson_start')
    template_name = 'index.html'
    paginate_by = 6


class About(generic.ListView):
    model = Coach
    queryset = Coach.objects.filter(status=1).order_by('first_name')
    template_name = 'about.html'
    paginate_by = 6


class Contact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_success')


class LessonDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        coach = lesson.coach
        feedbacks = lesson.feedbacks.filter(approved=True).order_by('-created_on')
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
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        coach = lesson.coach
        feedbacks = lesson.feedbacks.filter(approved=True).order_by('-created_on')
        liked = False
        booking_form = BookingForm()
        user = get_user(request)
        submitted_feedback = False
        submitted_booking = False
        
        if lesson.likes.filter(id=self.request.user.id).exists():
            liked = True

        if user.is_authenticated:
            has_booking = self.user_has_booked(user, lesson)
            if has_booking:
                # User has already made a booking, return an error response
                messages.error(request, "You have already booked this lesson! Please check My Bookings page.")
            else:
                feedback_form = FeedbackForm(data=request.POST)
                booking_form = BookingForm(data=request.POST)

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

                if booking_form.is_valid():
                    booking = booking_form.save(commit=False)
                    booking.lesson = lesson
                    booking.username = request.user
                    booking.save()
                    submitted_booking = True
                    messages.success(request, 'Thank you for your booking request!')
                else:
                    booking_form = BookingForm()
                    print("booking failed")

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
            },
        )

    def user_has_booked(self, user, lesson):
        return Booking.objects.filter(lesson=lesson, username=user).exists()


class LessonLike(View):

    def post(self, request, slug, *args, **kwargs):
        lesson = get_object_or_404(Lesson, slug=slug)

        if lesson.likes.filter(id=request.user.id).exists():
            lesson.likes.remove(request.user)
        else:
            lesson.likes.add(request.user)

        return HttpResponseRedirect(reverse('lesson_detail', args=[slug]))


class MyBookings(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        current_time = timezone.now()

        future_bookings = Booking.objects.filter(username=user,
            lesson__lesson_start__gt=current_time)
        past_bookings = Booking.objects.filter(username=user,
            lesson__lesson_start__lte=current_time) 
        return render(
            request,
            "my_bookings.html",
            {
                "future_bookings": future_bookings,
                "past_bookings": past_bookings,
            },
        )

    def post(self, request, *args, **kwargs):
        booking_id = request.POST.get('booking_id')
        if booking_id:
            # Find the booking with the provided ID
            booking = Booking.objects.filter(id=booking_id).first()

            if booking and booking.username == request.user:
                # Cancel the booking
                booking.delete()
                messages.success(request, 'Booking canceled successfully.')
            else:
                messages.error(request, 'Unable to cancel the booking.')
                
        return HttpResponseRedirect(reverse('my_bookings'))