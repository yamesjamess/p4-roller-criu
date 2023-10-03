from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Lesson


class LessonList(generic.ListView):
    model = Lesson
    queryset = Lesson.objects.filter(status=1).order_by('lesson_level')
    template_name = 'index.html'
    paginate_by = 6


class LessonDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Lesson.objects.filter(status=1)
        lesson = get_object_or_404(queryset, slug=slug)
        feedbacks = lesson.feedbacks.filter(approved=True).order_by('created_on')
        liked = False
        if lesson.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "lesson_detail.html",
            {
                "lesson": lesson,
                "feedbacks": feedbacks,
                "liked": liked,
            },
        )
