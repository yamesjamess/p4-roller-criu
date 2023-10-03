from . import views
from django.urls import path

urlpatterns = [
    path('', views.LessonList.as_view(), name='home'),
    path('<slug:slug>/', views.LessonDetail.as_view(), name='lesson_detail'),
]