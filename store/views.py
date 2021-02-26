from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Category,Products,Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignupForm

from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views import View
from cart.cart import Cart
import random



class Index(View):


    def get(self,request):
        product = None

        categories=Category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
            product=Products.objects.filter(category=categoryID)
        else:
            product = Products.objects.all()
        return render(request,'store/home.htm',{'products':product,'categories':categories})



def signUp(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        
        if fm.is_valid():
            error_message=None
            name=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            phone=fm.cleaned_data['phone']
            password1=fm.cleaned_data['password1']
            password2=fm.cleaned_data['password2']


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
                return HttpResponseRedirect('/login/')
            else:
                fm = SignupForm()
                return render(request,'store/signup.htm',{'error':error_message,'form':fm})
    else:
        fm = SignupForm()
    return render(request,'store/signup.htm',{'form':fm})

    

# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data= request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In SuccessFully')
                    return HttpResponseRedirect('/')
        else:
            form=LoginForm()
        return render(request,'store/login.htm',{'form':form})
    else:
        return HttpResponseRedirect('/')


# @method_decorator(login_required,name='dispatch')
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/logoutView/')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    



def userlogoutView(request):
    return render(request,'store/logoutView.htm')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)



@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("homepage")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("homepage")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("homepage")

@login_required(login_url="/login")
def item_remove(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    product=Products.objects.all()
    return render(request, 'store/cart_detail.htm',{'products':product})




def checkout(request):
    return render(request,'store/checkout.htm')