from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Coach, Lesson, Feedback, Booking, Contact



@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):

    list_filter = ('first_name', 'last_name', 'specialization')
    list_display = ('pk', 'first_name', 'last_name', 'years_of_experience', 'specialization', 'status')
    list_display_links = ('first_name',)
    search_fields = ['first_name', 'last_name', 'specialization']
    summernote_fields = ('bio')


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('pk', 'title', 'slug', 'coach', 'lesson_start', 'created_on', 'status')
    list_display_links = ('title',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('username', 'body', 'lesson_id', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    list_display_links = ('username',)
    search_fields = ['username', 'user_id', 'body']
    actions = ['approved_feedback', 'unapproved_feedback']

    def approved_feedback(self, request, queryset):
        queryset.update(approved=True)

    def unapproved_feedback(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('lesson', 'username', 'places_reserved', 'approved')
    list_display_links = ('lesson',)
    list_filter = ('lesson', 'approved')
    search_fields = ('lesson', 'approved')
    actions = ['approve_booking', 'unapprove_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved='approved')

    def unapprove_booking(self, request, queryset):
        queryset.update(approved='not_approved')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'contact_message', 'created_on')
    list_filter = ('name', 'email', 'created_on')
    list_display_links = ('name',)
    search_fields = ['name', 'email', 'contact_message', 'created_on']


