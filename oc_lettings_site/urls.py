import os

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

if 'RENDER' in os.environ:
    prod_admin = os.getenv('PRODUCTION_ADMIN')
    path_admin = path(prod_admin + '/', admin.site.urls)
else:
    path_admin = path('admin/', admin.site.urls)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('profiles.urls')),
    path('', include('lettings.urls')),
    path_admin,
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
