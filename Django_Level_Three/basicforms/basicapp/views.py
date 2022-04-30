from traceback import format_list
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from basicapp import forms
from basicapp.forms import FormName
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html', context={})

def thanks(request):
    return HttpResponse('THANKS')

def formpage(request):
    form = FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])

            return HttpResponseRedirect('/thanks')
        # else:
        #     form = forms.FormName()
        #     print("FORM IS NOT VALID!!")
        
    
    return render(request, 'basicapp/form_page.html', context={'inside_form': form})