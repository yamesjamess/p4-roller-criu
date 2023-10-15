from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Lesson, Coach, Feedback
from .forms import FeedbackForm


class LessonList(generic.ListView):
    model = Lesson
    queryset = Lesson.objects.filter(status=1).order_by('lesson_time')
    template_name = 'index.html'
    paginate_by = 6


class About(generic.ListView):
    model = Coach
    queryset = Coach.objects.filter(status=1).order_by('first_name')
    template_name = 'about.html'
    paginate_by = 6


class LessonDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        coach = lesson.coach
        feedbacks = lesson.feedbacks.filter(approved=True).order_by('-created_on')
        liked = False
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
                "feedback_form": FeedbackForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        feedbacks = lesson.feedbacks.filter(approved=True).order_by('-created_on')
        liked = False
        if lesson.likes.filter(id=self.request.user.id).exists():
            liked = True

        feedback_form = FeedbackForm(data=request.POST)

        if feedback_form.is_valid():
            feedback_form.instance.email = request.user.email
            feedback_form.instance.name = request.user.username
            feedback_form.instance.username_id = request.user.id
            feedback = feedback_form.save(commit=False)
            feedback.lesson = lesson
            feedback.save()
        else:
            feedback_form = FeedbackForm()

        return render(
            request,
            "lesson_detail.html",
            {
                "lesson": lesson,
                "feedbacks": feedbacks,
                "submitted_feedback": True,
                "feedback_form": FeedbackForm(),
                "liked": liked
            },
        )


class LessonLike(View):

    def post(self, request, slug, *args, **kwargs):
        lesson = get_object_or_404(Lesson, slug=slug)

        if lesson.likes.filter(id=request.user.id).exists():
            lesson.likes.remove(request.user)
        else:
            lesson.likes.add(request.user)

        return HttpResponseRedirect(reverse('lesson_detail', args=[slug]))


