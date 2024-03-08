from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appDev(request):
    return render(request,'appDev.html')

def contact(request):
    return render(request,'contact.html')

def hiring(request):
    return render(request,'hiring.html')

def learning(request):
    return render(request,'learning.html')

def portfolio(request):
    return render(request,'portfolio.html')

def team(request):
    return render(request,'team.html')

def terms(request):
    return render(request,'terms.html')

def uxui(request):
    return render(request,'uxui.html')

def webDev(request):
    return render(request,'webDev.html')

def page_not_found(request):
    return render(request,'404.html')