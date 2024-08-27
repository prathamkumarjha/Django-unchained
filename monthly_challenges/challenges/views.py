from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("This works")

def feb(request):
    return HttpResponse("This is for feburary")

def monthly_challenge(request, month):
    if month == "january" :
        return HttpResponse("This is january")
    elif month == "feburary" :
         return HttpResponse("this is for month of feburary")
    elif month == "feburary" :
         return HttpResponse("this is for month of feburary")
    elif month == "march" :
             return HttpResponse("this is for month of march")
    elif month == "april" :
             return HttpResponse("this is for month of may")
    elif month == "may":
           return HttpResponse("this is for month may")
    elif month == "june" :
             return HttpResponse("this is for month of june")
    elif month == "july" :
             return HttpResponse("this is for month of july")
    elif month == "august" :
             return HttpResponse("this is for month of august")
    elif month == "september" :
             return HttpResponse("this is for month of september")
    elif month == "october" :
             return HttpResponse("this is for month of october")
    elif month == "november" :
             return HttpResponse("this is for month of november")
    elif month == "december":
           return HttpResponse("this is for month of december")
    else:
           return HttpResponseNotFound("this month is not supported")