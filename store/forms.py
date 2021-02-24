from django import forms
from django.core import validators
from .models import Customer
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields =['name','email','phone','password','confirm_password']
#         widgets={'name':forms.TextInput(attrs={'autofocus': True,'class':"form-control form-control-sm",'min':'0'}),
#                     'email':forms.EmailInput(attrs={'class':"form-control form-control-sm",'placeholder':'Example@example.com'}),
#                     'phone':forms.NumberInput(attrs={'class':"form-control form-control-sm"}),
#                     'password':forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}),
#                     'confirm_password':forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}),
#                 }
    

# class LoginForm(forms.Form):
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,'class':"form-control form-control-sm"}))
    
    password=forms.CharField(label=_("Password"), strip= False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control form-control-sm'}))





class SignupForm(UserCreationForm):
    phone=forms.IntegerField(label='Phone',widget=forms.NumberInput(attrs={'class':"form-control form-control-sm"}))

    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}))

    password2= forms.CharField(label='Confirm_Password', widget=forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}))

    class Meta:
        model = User
        fields =['username','email','phone','password1','password2']
        labels= {'email':'Email','username':'User Name'}
        widgets={'username':forms.TextInput(attrs={'autofocus': True,'class':"form-control form-control-sm",'min':'0'}),
                    'email':forms.EmailInput(attrs={'required':True ,'class':"form-control form-control-sm",'placeholder':'Example@example.com'}),
                }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
    
