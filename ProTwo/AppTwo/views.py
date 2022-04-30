from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import User
# Create your views here.
def home(request):
    # return HttpResponse("<em>My Second App</em>")
    my_dict = {'insert_me':"Hello! I am from views.py!"}
    return render(request, 'AppTwo/home.html', context=my_dict)

def Users(request):
    # return HttpResponse("A game")
    Users_info = User.objects.order_by('first_name')
    email_dict = {'users_infos': Users_info}
    return render(request, 'AppTwo/users.html', context=email_dict)

def homepage(request):
    return HttpResponse("Go to 'AppTwo/Users' to see users info.")