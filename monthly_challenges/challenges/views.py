from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("This works")

def feb(request):
    return HttpResponse("This is for February")

def monthly_challenge(request, month_string):
    challenges = {
        "january": "This is for January",
        "february": "This is for February",
        "march": "This is for March",
        "april": "This is for April",
        "may": "This is for May",
        "june": "This is for June",
        "july": "This is for July",
        "august": "This is for August",
        "september": "This is for September",
        "october": "This is for October",
        "november": "This is for November",
        "december": "This is for December"
    }

    response_text = f"<h1>{challenges.get(month_string.lower())}</h1>"
    
    if response_text:
        return HttpResponse(response_text)
    else:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenge_by_number(request, month_integer):
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    
    if 1 <= month_integer <= 12:
        month_name = months[month_integer - 1]
        redirected_path = reverse("month_challenge", args=[month_name])  # Correct URL name
        return HttpResponseRedirect(redirected_path)
    else:
        return HttpResponseNotFound("Invalid month number")
