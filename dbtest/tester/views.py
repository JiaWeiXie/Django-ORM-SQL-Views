from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.


def buys(request):
    m=ViewerProduct.objects.using('mysql').get(proNo='P001')
    d=model_to_dict(m, fields=['price', 'proName', 'proNo'])
    return JsonResponse({'text':d})

