from decimal import Context
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context={
        "items":Item.objects.all()
    }
    return render(request,'store.html',context)

