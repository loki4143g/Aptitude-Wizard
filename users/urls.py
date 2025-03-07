from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
   path('register/', views.user_register, name='register'),
   path('login/', views.user_login, name='login'),
   path('logout/',views.user_logout, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('edit-profile/', views.editprofile, name='edit-profile'),
]