from . import views
from django.urls import path

urlpatterns = [
    path('', views.LessonList.as_view(), name='home'),
    path('<slug:slug>/', views.LessonDetail.as_view(), name='lesson_detail'),
    path('like/<slug:slug>/', views.LessonLike.as_view(), name='lesson_like'),
]