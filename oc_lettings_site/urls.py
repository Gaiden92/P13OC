import os

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

path_admin = path('secret0208/', admin.site.urls) if 'RENDER' in os.environ else path('admin/', admin.site.urls)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('profiles.urls')),
    path('', include('lettings.urls')),
    path_admin,
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
