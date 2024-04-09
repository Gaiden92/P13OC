from django.urls import path

from profiles import views as profiles_views


urlpatterns = [
    path('profiles/', profiles_views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
]
