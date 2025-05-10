from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'homepage.html')