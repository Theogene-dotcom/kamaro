from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("my name is Theogene Musengimana","imbwa gusa!!!!!!!!!!!!!!!!!!!")