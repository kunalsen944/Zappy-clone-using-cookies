from zappyapp import views
from django.urls import path
from django.conf import settings


app_name='zappyapp'
urlpatterns = [
    path('', views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('updateprofile',views.cprofile,name='uprofile'),
    path('profile',views.profile,name='profile'),
    path('details/<id>',views.productsdetails),
    path('search',views.search,name='search'),
    path('ReadyToeat', views.readytoeat,name='readytoeat'),
    path('ReadyToCook', views.readytocook,name='readytocook'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('cartview',views.cart_view,name='cartview'),
    path('cartitems',views.cartitems,name='cartitems'),
    path('cartupdates',views.cartupdates,name='cartupdates'),
    path('cartdel',views.cartdel,name='cartdel'),
    path('checkout',views.checkout,name='checkout'),
    path('orderhistory',views.orderh,name='orderhistory'),
    ]
