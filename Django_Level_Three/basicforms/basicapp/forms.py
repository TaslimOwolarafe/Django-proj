import email
# from ssl import VerifyFlags
from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() not in ['z', 't']:
        raise forms.ValidationError("Name needs to start with a Z or T.")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
            widget=forms.HiddenInput,
            validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError('MAKE SURE THE EMAILS MATCH!')

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #     return botcatcher

    