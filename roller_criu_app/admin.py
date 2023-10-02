from django.contrib import admin
from .models import Class, Feedback
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Class)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Feedback)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'class_id', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'user_id', 'body']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)