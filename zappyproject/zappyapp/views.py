from django.shortcuts import render,reverse,redirect
from django.contrib.auth.forms import UserCreationForm
from zappyapp.models import Product,Customer,Order
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from zappyapp.forms import CustomerUpdate,Checkout
# Create your views here.


def home(request):
    products=Product.objects.all().order_by('-id')
    return render(request,'zappyapp/home.html',{'products':products})

def rte(request):
    products=Product.objects.filter(cat_choice='rte')
    return render(request,'zappyapp/rte.html',{'products':products})

def rtc(request):
    products=Product.objects.filter(cat_choice='rtc')
    return render(request,'zappyapp/rtc.html',{'products':products})


def registration(request):
    sform=UserCreationForm(request.POST or None)
    if sform.is_valid():
        new_user=sform.save()
        return HttpResponseRedirect(reverse('zappyapp:home'))

    return render(request,'zappyapp/registration.html',{'sform':sform})

@login_required
def profile(request):
    return render(request, 'zappyapp/profile.html')


@login_required
def cprofile(request):
    if request.method == 'POST':
        cu_form = CustomerUpdate(request.POST,request.FILES,instance=request.user.customer)
        if cu_form.is_valid():
            cu_form.save()
            return HttpResponseRedirect(reverse('zappyapp:profile'))
    else:
        cu_form = CustomerUpdate(request.POST,request.FILES,instance=request.user.customer)
    return render(request, 'zappyapp/cprofile.html',{'cu_form':cu_form})


def productsdetails(request,id):
    products=Product.objects.get(id=id)
    return render(request,'zappyapp/productdetails.html',{'products':products})

def search(request):
    query=request.GET.get('q')
    products=Product.objects.filter(pname__icontains=query)
    if products is not None:
        return render(request,'zappyapp/home.html',{'products':products})
    else:
        return HttpResponseRedirect(reverse('zappyapp:home'))

def addtocart(request):
    response=HttpResponseRedirect(reverse('zappyapp:cartr'))
    id=request.POST.get('product_id')
    item=request.POST.get('items')
    if id in request.COOKIES.keys():
        items=int(request.COOKIES.get(id))
        item=int(item)+items
        response.set_cookie(id,item)
    else:
        response.set_cookie(id,item)
    return response

def cart_view(request):
    products=Product.objects.all()
    price=[]
    img=[]
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            img.append(Product.objects.get(id=i).image.url)
            price.append(Product.objects.get(id=i).price*int(j))
    total=sum(price)
    dict={'price':price,'total':total,'img':img}
    if not request.COOKIES.items():
        price=[]
        img=[]
        total=0
    return render(request,'zappyapp/cartview.html',context=dict)

def cart(request):
    length=0
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            length+=1
    response=HttpResponseRedirect(reverse('zappyapp:updations'))
    response.set_cookie('length',length)
    return response

def cartupdates(request):
    response=HttpResponseRedirect(reverse('zappyapp:cartr'))
    id=request.GET.get('product_id')
    item=request.GET.get('items')
    if id in request.COOKIES.keys():
        response.set_cookie(id,item)
    return response

def updations(request):
    return HttpResponseRedirect(reverse('zappyapp:cartview'))

def cartdel(request):
    response=HttpResponseRedirect(reverse('zappyapp:cartr'))
    id=request.GET.get('product_id')
    if id in request.COOKIES.keys():
        response.delete_cookie(id)
    return response

@login_required
def orderh(request):
    order=Order.objects.filter(users=request.user).order_by('-id')
    return render(request, 'zappyapp/orderhistory.html',{'order':order})


@login_required
def checkout(request):
    products=[]
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            products.append(Product.objects.get(id=i).pname)
    if request.method == 'POST':
        ch_form = Checkout(request.POST)
        if ch_form.is_valid():
            test=ch_form.save(commit=False)
            test.users=request.user
            test.pids=products
            test.save()
            response=render(request,'zappyapp/sucess.html')
            for i in request.COOKIES.keys():
                if i.isdigit() or i=='length':
                    response.delete_cookie(i)
            return response
    else:
        ch_form = Checkout(request.POST)
    return render(request, 'zappyapp/checkout.html',{'ch_form':ch_form})
