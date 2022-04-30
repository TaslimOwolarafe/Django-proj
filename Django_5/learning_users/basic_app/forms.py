# from xml.dom.minidom import Attr
from django import forms
from basic_app.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =['username','email','password']

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "id": "username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "id": "email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "id": "password"}),
        }
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']

        widgets = {
            "portfolio_site": forms.URLInput(attrs={"class": "form-control", "id": "portfolio"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control", "id": "picture"}),
        }