from django import forms
from django.forms import extras
from datetime import date


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name',
                            widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Surname',
                            widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(date.today().year, 1900, -1)), label='Date of Birth')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.dob = self.cleaned_data['dob']
        user.save()
