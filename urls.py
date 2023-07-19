from django.urls import path
from. views import index, top_sellers, register, login, profile

urlpatterns = [
    path('', index, name='/'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('register/', register, name='register'),
    path('login/', register, name='login'),
    path('profile/', register, name='profile'),


]
