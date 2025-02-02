from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('categories/<str:section>/', views.category_view, name='category'),
    path('questions/<str:name>/', views.load_questions, name='questions-page'),
]