from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = 'roller_criu_project.views.handler404'
handler500 = 'roller_criu_project.views.handler500'
handler403 = 'roller_criu_project.views.handler403'
handler405 = 'roller_criu_project.views.handler405'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('roller_criu_app.urls'), name='roller_criu_urls'),
    path('accounts/', include('allauth.urls')),
]
