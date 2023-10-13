from django.contrib import admin
from .models import Coach, Lesson, Feedback, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):

    list_filter = ('first_name', 'last_name', 'specialization')
    list_display = ('pk', 'first_name', 'last_name', 'years_of_experience', 'specialization', 'status')
    search_fields = ['first_name', 'last_name', 'specialization']
    summernote_fields = ('bio')


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('pk', 'title', 'slug', 'coach', 'lesson_time', 'created_on', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('username', 'body', 'lesson_id', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['username', 'user_id', 'body']
    actions = ['approved_feedback', 'unapprove_feedback']

    def approved_feedback(self, request, queryset):
        queryset.update(approved=True)

    def unapprove_feedback(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('lesson', 'username', 'approved')
    list_filter = ('lesson', 'approved')
    search_fields =('lesson', 'approved')
    actions = ['approve_booking', 'unapprove_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)

    def unapprove_booking(self, request, queryset):
        queryset.update(approved=False)
