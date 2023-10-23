from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.LessonList.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
    path('my_bookings/', views.MyBookings.as_view(), name='my_bookings'),
    path('<slug:slug>/', views.LessonDetail.as_view(), name='lesson_detail'),
    path('like/<slug:slug>/', login_required(views.LessonLike.as_view()), name='lesson_like'),
    
]