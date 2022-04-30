from basicapp import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path("formpage/", views.formpage, name= 'form_page'),
    path('thanks/', views.thanks, name='thankyou')
]