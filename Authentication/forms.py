from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ImageField, FileInput, DateInput

from .models import User, UserProfile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']


    #     widgets = {
    #     'username' : forms.TextInput (attrs= {'placeholder': 'Enter your username'}),
    #     'email' : forms.TextInput (attrs= {'placeholder': 'Enter your email...'}),
    #     'password1' : forms.TextInput (attrs= {'placeholder': 'Enter your password...'}),
    #     'password2' : forms.TextInput (attrs= {'placeholder': 'repeat password...'}),
        
    # }


class ProfileForm(forms.ModelForm):

    Profile_Picture = ImageField (widget= FileInput)
    Cover_Photo = ImageField (widget= FileInput)
    DOB = forms.DateField (widget = forms.DateInput (attrs= {'type': 'date'}))


    class Meta:
        model = UserProfile

        fields = ['First_Name', 'Middle_Name', 'Last_Name', 'Profile_Picture', 'Cover_Photo', 'DOB', 'Address_Line1', 'Address_Line2',
                  'Nationality', 'City', 'Zip_or_Postcode', 'Mobile_Number']
        

        widgets = {
        'First_Name' : forms.TextInput (attrs= {'placeholder': 'Enter your first name...'}),
        'Middle_Name' : forms.TextInput (attrs= {'placeholder': 'Enter your middle name...'}),
        'Last_Name' : forms.TextInput (attrs= {'placeholder': 'Enter your last name...'}),
        'Address_Line1' : forms.TextInput (attrs= {'placeholder': 'Address one...'}),
        'Address_Line2' : forms.TextInput (attrs= {'placeholder': 'Address two...'}),
        'Nationality' : forms.TextInput (attrs= {'placeholder': 'Enter your country...'}),
        'City' : forms.TextInput (attrs= {'placeholder': 'Enter your city...'}),
        'Zip_or_Postcode' : forms.TextInput (attrs= {'placeholder': 'Enter your zip or post code...'}),
        'Mobile_Number' : forms.TextInput (attrs= {'placeholder': 'Enter your mobile number...'}),
    }