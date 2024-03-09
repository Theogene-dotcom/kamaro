from django.shortcuts import render
from django.contrib import messages
from kamarop.models import contactmodel

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

def insertcontact(request):
    if request.method=="POST":
        if request.POST.get('userFirstName') and request.POST.get('userLastName') and request.POST.get('userEmail') and request.POST.get('contactNumber') and request.POST.get('compName') and request.POST.get('projectTitle') and request.POST.get('projectDisp'):
            saverecord=contactmodel()
            saverecord.userFirstName=request.POST.get('userFirstName')
            saverecord.userLastName=request.POST.get('userLastName')
            saverecord.userEmail=request.POST.get('userEmail')
            saverecord.contactNumber=request.POST.get('contactNumber')
            saverecord.compName=request.POST.get('compName')
            saverecord.projectTitle=request.POST.get('projectTitle')
            saverecord.projectDisp=request.POST.get('projectDisp')
            saverecord.save()
            messages.success(request,'User'+saverecord.userFirstName+'is saved successfully!')
            return render(request,'showcontact.html')
        
    else:
        
            return render(request,'showcontact.html')
        
def showcontact(request):
    showall=contactmodel.objects.all()
    return render(request,'showcontact.html',{"data":showall})