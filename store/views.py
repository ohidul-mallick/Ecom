from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Category,Products,Customer,Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignupForm

from .forms import LoginForm,OrderForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views import View
from cart.cart import Cart
import random
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User

class Home(View):
    def get(self,request):
        return render(request,'store/home_copy.html')




class Index(View):


    def get(self,request):
        product = None
        

        categories=Category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
            product=Products.objects.filter(category=categoryID)
        else:
            product = Products.objects.all()
        return render(request,'store/home.html',{'products':product,'categories':categories})



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
                return render(request,'store/signup.html',{'error':error_message,'form':fm})
    else:
        fm = SignupForm()
    return render(request,'store/signup.html',{'form':fm})

    

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
        return render(request,'store/login.html',{'form':form})
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
    return render(request,'store/logoutView.html')

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
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

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
    return render(request, 'store/cart_detail.html',{'products':product})






class checkoutView(View):

    def get(self,request):
        od=OrderForm()
        return render(request,'store/checkout.html',{'orders':od})
    
    def post(self,request):
        od=OrderForm(request.POST)

        cart=request.session.get('cart')
        cartObj=cart.values()

        # print(cartObj)
        for item in cartObj:
            userid = item['userid']
            Price=item['price']
            Quantity=item['quantity']
            productName=item['name']
            product=Products.objects.get(name=productName)


            customer=User.objects.get(id=userid)
            error_message=None
            if od.is_valid():

                
                fname=od.cleaned_data['first_name'] 
                lname=od.cleaned_data['last_name'] 
                email=od.cleaned_data['email'] 
                address=od.cleaned_data['address'] 
                phone=od.cleaned_data['phone'] 
                dt=date.today() 
                # Error Message Section

                if len(fname)<2 or len(lname)<2:
                    error_message ='Enter Valid Name'
                if len(str(phone))<6:
                    error_message ='Enter Valid Phone Number'
                if len(address)<6:
                    error_message ='Enter Valid Address'
                # End of Message Section
                if not error_message:
                    order=Order(product=product,customer=customer,first_name=fname,last_name=lname,email=email,quantity=Quantity,price=Price,address=address,phone=phone,date=dt)
                    order.save()
                    del request.session[settings.CART_SESSION_ID]
                    messages.success(request,'Order Placed Successfully...')
                    return HttpResponseRedirect('/order/')
                else:
                    # print(error_message)
                    # print(len(fname))
                    od=OrderForm()
                    return render(request,'store/checkout.html',{'error':error_message,'orders':od})
            else:
                error_message='Please Enter Valid Details'
                od=OrderForm()
                return render(request,'store/checkout.html',{'error':error_message,'orders':od})



@login_required(login_url="/login")
def orderDetail(request):
    order=Order.objects.all()
    product = Products.objects.all()

    print(order.query)

    return render(request, 'store/order.html',{'products':product,'orders':order})


def profileDetail(request):
    username=request.user.username
    print(username)
    return render(request,'store/profile.html',{'name':username})