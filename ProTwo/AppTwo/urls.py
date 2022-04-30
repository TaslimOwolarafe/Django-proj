from AppTwo import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("Users/", views.Users, name="users"),
]