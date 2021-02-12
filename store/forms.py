from django import forms
from django.core import validators
from .models import Customer
class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name','email','phone','password','confirm_password']
        widgets={'name':forms.TextInput(attrs={'class':"form-control form-control-sm",'min':'0'}),
                    'email':forms.EmailInput(attrs={'class':"form-control form-control-sm",'placeholder':'Example@example.com'}),
                    'phone':forms.NumberInput(attrs={'class':"form-control form-control-sm"}),
                    'password':forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}),
                    'confirm_password':forms.PasswordInput(attrs={'class':"form-control form-control-sm","oncopy":"return false","onpaste":"return false"}),


                }
    
        # def clean(self):
        #     cleaned_data = super().clean()
        #     nm=self.cleaned_data['name']
        #     pwd1=self.cleaned_data['password']
        #     pwd2=self.cleaned_data['confirm_password']
        #     if pwd1 != pwd2:
        #         raise forms.ValidationError('Password Does not match')
            
        #     if len(pwd1) <6:
        #         raise forms.ValidationError('Password Must Be Greater than or Equal to 6 Character Long')
        #     return pwd1

        #     if len(nm) <6:
        #         raise forms.ValidationError('Name Must Be Greater than or Equal to 6 Character Long')
        #     return nm


