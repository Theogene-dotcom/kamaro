from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request,'kigalicoding/index.html')

def about(request):
    return render(request,'kigalicoding/about.html')

def appDev(request):
    return render(request,'kigalicoding/appDev.html')

def contact(request):
    return render(request,'kigalicoding/contact.html')

def hiring(request):
    return render(request,'kigalicoding/hiring.html')

def learning(request):
    return render(request,'kigalicoding/learning.html')

def portfolio(request):
    return render(request,'kigalicoding/portfolio.html')

def team(request):
    return render(request,'kigalicoding/team.html')

def terms(request):
    return render(request,'kigalicoding/terms.html')

def uxui(request):
    return render(request,'kigalicoding/uxui.html')

def webDev(request):
    return render(request,'kigalicoding/webDev.html')

def page_not_found(request):
    return render(request,'kigalicoding/404.html')