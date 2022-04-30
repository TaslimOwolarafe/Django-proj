from django.urls import path
from AppThree import views

urlpatterns = [
    path("", views.profile, name="Profile")
]