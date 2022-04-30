from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    # return HttpResponse("Hello world!")
    webapages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webapages_list}
    # index_dict = {'inside_index': 'This is an index Page'}
    return render(request, "first_app/index.html", context=date_dict)

def help(request):
    help_dict = {'inside_help': 'Help Page.'}
    return render(request, "first_app/help.html", context=help_dict)

def welcome(request):
    return HttpResponse("Welcome!")
