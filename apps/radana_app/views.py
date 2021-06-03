from decimal import Context
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render
from .models import *
from ..login_register.models import User

# Create your views here.
def index(request):       
        context={
            "item1":Item.objects.get(id=1),
            # "item2":Item.objects.get(id=2),
            # "item3":Item.objects.get(id=3),
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
# def checkout(request):
#     return render(request,'')
def logout(request):
    request.session.clear()
    return redirect ('http://127.0.0.1:8000/home/')

