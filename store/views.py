from django.shortcuts import render
from .models import Category,Products,Customer
from django.contrib import messages


def home(request):
    product = None
    categories=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Products.objects.filter(category=categoryID)
    else:
        product = Products.objects.all()
    return render(request,'store/home.htm',{'products':product,'categories':categories})



from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm


def signUp(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        
        if fm.is_valid():
            error_message=None
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            phone=fm.cleaned_data['phone']
            password1=fm.cleaned_data['password']
            password2=fm.cleaned_data['confirm_password']


            if len(name)<6:
                error_message ='Name Should be More than 6'

            elif len(str(phone))<10:
                error_message ='Enter Proper Phone Number'
            elif len(password1)<6:
                error_message ='Password Should be More than 6'

            elif password1 != password2:
                error_message ='Password Did Not Match'
            elif Customer.objects.filter(email=email).exists():
                error_message ='Email Already Exists'

            if not error_message:
                fm.save()
                messages.success(request,'Account Created Successfully...')
                fm = SignupForm()
            else:
                fm = SignupForm()
                return render(request,'store/signup.htm',{'error':error_message,'form':fm})
    else:
        fm = SignupForm()
    return render(request,'store/signup.htm',{'form':fm})