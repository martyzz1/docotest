from django import forms
from django.forms import extras


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Surname')
    dob = forms.DateField(widget=extras.SelectDateWidget, label='Date of Birth')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.dob = self.cleaned_data['dob']
        user.save()
