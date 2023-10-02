from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Class


class ClassList(generic.ListView):
    model = Class
    queryset = Class.objects.filter(status=1).order_by('class_level')
    template_name = 'index.html'
    paginate_by = 6

