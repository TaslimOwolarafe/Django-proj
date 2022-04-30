from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    # return HttpResponse("Welcome to Taslim's Profile Page.")
    return render(request, "AppThree/Profile.html", context= {'inside_Hello': 'Hello!'})


