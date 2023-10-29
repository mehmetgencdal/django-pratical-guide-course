from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

def index(request):
    
    months = list(monthly_challenges.keys())

    context = {
        "months": months
    }
    
    return render(request, "challenges/index.html", context)
    
def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirected_month = months[month-1]
        return HttpResponseRedirect(reverse("month-challenge", args=[redirected_month]))
    except:
        return HttpResponseNotFound("This month is not supported!")
        
        
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {
            "text": challenge_text,
            "month": month
        }
        return render(request, "challenges/challenge.html", context)
    except:
        raise Http404()