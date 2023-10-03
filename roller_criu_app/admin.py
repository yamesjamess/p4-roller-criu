from django.contrib import admin
from .models import Coach, Lesson, Feedback
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Coach)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('first_name', 'last_name', 'specialization')
    list_display = ('pk', 'first_name', 'last_name', 'years_of_experience', 'specialization', 'status')
    search_fields = ['first_name', 'last_name', 'specialization']
    summernote_fields = ('bio')


@admin.register(Lesson)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('pk', 'title', 'slug', 'coach', 'lesson_time', 'created_on', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Feedback)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'lesson_id', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'user_id', 'body']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)

