from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClassList.as_view(), name='home')
]