from django.shortcuts import render,HttpResponse 
import json

from .models import *

# Create your views here.
def index(request):
    return render(request,'index2.html')

def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Item.objects.filter(title=q)
        results = []
        print (q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


