from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Coach, Lesson, Feedback, Booking, Contact


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):
    """
    Admin class for the Coach model. This class extends SummernoteModelAdmin to enable
    rich text editing for the 'bio' field.

    Attributes:
        list_filter (tuple): Fields available for filtering in the admin list view.
        list_display (tuple): Fields to display in the admin list view.
        list_display_links (tuple): Fields to use as links in the list view.
        search_fields (list): Fields to search for in the admin list view.
        summernote_fields (tuple): Fields to enable the Summernote rich text editor for.
    """

    list_filter = ('first_name', 'last_name', 'specialization')
    list_display = ('pk', 'first_name', 'last_name',
                    'years_of_experience', 'specialization', 'status')
    list_display_links = ('first_name',)
    search_fields = ['first_name', 'last_name', 'specialization']
    summernote_fields = ('bio')


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    """
    Admin class for the Lesson model. This class extends SummernoteModelAdmin to enable
    rich text editing for the 'content' field.

    Attributes:
        list_filter (tuple): Fields available for filtering in the admin list view.
        list_display (tuple): Fields to display in the admin list view.
        list_display_links (tuple): Fields to use as links in the list view.
        search_fields (list): Fields to search for in the admin list view.
        prepopulated_fields (dict): Fields to automatically populate based on other fields.
        summernote_fields (tuple): Fields to enable the Summernote rich text editor for.
    """

    list_filter = ('status', 'created_on')
    list_display = ('pk', 'title', 'slug', 'coach',
                    'lesson_start', 'created_on', 'status')
    list_display_links = ('title',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Admin class for the Feedback model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields available for filtering in the admin list view.
        list_display_links (tuple): Fields to use as links in the list view.
        search_fields (list): Fields to search for in the admin list view.
        actions (list): Custom admin actions available for bulk processing of feedback.

    Methods:
        approved_feedback(request, queryset):
            Mark selected feedback as approved.

        unapproved_feedback(request, queryset):
            Mark selected feedback as unapproved.
    """

    list_display = ('username', 'body', 'lesson_id', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    list_display_links = ('username',)
    search_fields = ['username', 'user_id', 'body']
    actions = ['approved_feedback', 'unapproved_feedback']

    def approved_feedback(self, request, queryset):
        """
        Admin action to mark selected feedback as approved.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): Selected feedback objects to mark as approved.
        """

        queryset.update(approved=True)

    def unapproved_feedback(self, request, queryset):
        """
        Admin action to mark selected feedback as unapproved.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): Selected feedback objects to mark as unapproved.
        """

        queryset.update(approved=False)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the Booking model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_display_links (tuple): Fields to use as links in the list view.
        list_filter (tuple): Fields available for filtering in the admin list view.
        search_fields (tuple): Fields to search for in the admin list view.
        actions (list): Custom admin actions available for bulk processing of bookings.

    Methods:
        approve_booking(request, queryset):
            Approve selected bookings.

        unapprove_booking(request, queryset):
            Unapprove selected bookings.
    """

    list_display = ('lesson', 'username', 'places_reserved', 'approved')
    list_display_links = ('lesson',)
    list_filter = ('lesson', 'approved')
    search_fields = ('lesson', 'approved')
    actions = ['approve_booking', 'unapprove_booking']

    def approve_booking(self, request, queryset):
        """
        Admin action to approve selected bookings.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): Selected booking objects to approve.
        """

        queryset.update(approved='approved')

    def unapprove_booking(self, request, queryset):
        """
        Admin action to unapprove selected bookings.

        Args:
            request (HttpRequest): The request object.
            queryset (QuerySet): Selected booking objects to unapprove.
        """

        queryset.update(approved='not_approved')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for the Contact model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields available for filtering in the admin list view.
        list_display_links (tuple): Fields to use as links in the list view.
        search_fields (list): Fields to search for in the admin list view.
    """
    
    list_display = ('name', 'email', 'contact_message', 'created_on')
    list_filter = ('name', 'email', 'created_on')
    list_display_links = ('name',)
    search_fields = ['name', 'email', 'contact_message', 'created_on']
