from django.urls import path

from . import views
from profiles import views as profiles_views


urlpatterns = [
    path('profiles/', profiles_views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
]
