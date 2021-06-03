from decimal import Context
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render
from .models import *
from ..login_register.models import User

# Create your views here.
def index(request):       
        context={
            "item1":Item.objects.get(id=1),
            "item2":Item.objects.get(id=2),
            "item3":Item.objects.get(id=3),
        }
        return render(request,'store.html',context)
def item_detailes(request,item_id):
    context={
        "item":Item.objects.get(id=item_id)
    }
    return render(request,'item.html',context)
def items(request):
    context={
        'items':Item.objects.all()
    }
    return render (request,'shop.html',context)
def add_to_cart(request,item_id):
    current_user=User.objects.get(id=request.session['user_id'])
    added_item=Item.objects.get(id=item_id)
    Cart.user.add(current_user)
    Cart.items.add(added_item)   
    return redirect('/items')
def checkout(request):
    user=User.objects.get(id=request.session['user_id'])
    context={
        'order':Cart.items
    }
    return render(request,'checkout.html',context)
def logout(request):
    request.session.clear()
    return redirect ('/welcome')

