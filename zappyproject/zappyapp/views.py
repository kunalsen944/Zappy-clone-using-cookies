from django.shortcuts import render,reverse,redirect
from django.contrib.auth.forms import UserCreationForm
from zappyapp.models import Product,Customer,Order
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from zappyapp.forms import CustomerUpdate,Checkout



def home(request):
    products=Product.objects.all().order_by('-id') # Query to get all Product in decreasing order by id
    return render(request,'zappyapp/home.html',{'products':products})

def readytoeat(request):
    products=Product.objects.filter(cat_choice='rte').order_by('-id') # Query to get all Product in readytoeat category in decreasing order by id
    return render(request,'zappyapp/rte.html',{'products':products})

def readytocook(request):
    products=Product.objects.filter(cat_choice='rtc').order_by('-id') # Query to get all Product in readytoeat category in decreasing order by id
    return render(request,'zappyapp/rtc.html',{'products':products})

def productsdetails(request,id):
    products=Product.objects.get(id=id) # Query to get a Single Product in all products using an id
    return render(request,'zappyapp/productdetails.html',{'products':products})

def registration(request):
    sform=UserCreationForm(request.POST or None)
    if sform.is_valid():
        new_user=sform.save()
        return HttpResponseRedirect(reverse('zappyapp:home'))

    return render(request,'zappyapp/registration.html',{'sform':sform})

def search(request):
    query=request.GET.get('q')
    products=Product.objects.filter(pname__icontains=query) # Search Query to search products using their Name
    if products is not None:
        return render(request,'zappyapp/home.html',{'products':products})
    else:
        return HttpResponseRedirect(reverse('zappyapp:home'))

# Cart CRUD Views Started

def addtocart(request):
    response=HttpResponseRedirect(reverse('zappyapp:cartitems'))
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
    pname=[]
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            img.append(Product.objects.get(id=i).image.url)
            pname.append(Product.objects.get(id=i).pname)
            price.append(Product.objects.get(id=i).price*int(j))
    total=sum(price)
    dict={'price':price,'total':total,'img':img,'pname':pname}
    if not request.COOKIES.items():
        price=[]
        img=[]
        pname=[]
        total=0
    return render(request,'zappyapp/cartview.html',context=dict)


def cartitems(request):
    length=0
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            length+=1
    response=updations(request)
    response.set_cookie('length',length)
    return response


def cartupdates(request):
    response=cartitems(request)
    id=request.GET.get('product_id')
    item=request.GET.get('items')
    if id in request.COOKIES.keys():
        response.set_cookie(id,item)
    return response


def updations(request):
    return HttpResponseRedirect(reverse('zappyapp:cartview'))


def cartdel(request):
    response=cartitems(request)
    id=request.GET.get('product_id')
    if id in request.COOKIES.keys():
        response.delete_cookie(id)
    return response

# Cart CRUD Ended

# login Required View Started
@login_required
def orderh(request):
    order=Order.objects.filter(users=request.user).order_by('-id')
    return render(request, 'zappyapp/orderhistory.html',{'order':order})


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

@login_required
def checkout(request):
    products=[]
    add=Customer.objects.get(customer=request.user).cust_address
    for i,j in request.COOKIES.items():
        if i.isdigit() and j.isdigit():
            products.append(Product.objects.get(id=i).pname)
    if request.method == 'POST':
        ch_form = Checkout(request.POST)
        if ch_form.is_valid():
            test=ch_form.save(commit=False)
            if len(test.delievery_address):
                pass
            else:
                if add is None:
                    return HttpResponseRedirect(reverse('zappyapp:uprofile'))
                else:
                    test.delievery_address=add
            test.users=request.user
            test.pids=products
            test.save()
            response=render(request,'zappyapp/sucess.html')
            for i in request.COOKIES.keys():
                if i.isdigit() or i=='length':
                    response.delete_cookie(i)
            return response
    else:
        ch_form = Checkout()
    return render(request, 'zappyapp/checkout.html',{'ch_form':ch_form})
# Login Required Views Ended
