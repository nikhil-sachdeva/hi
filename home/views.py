from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'home/home.html')

def contact(request):
    return render(request,'home/contact.html')

def draw(request):
    return render(request,'home/draw.html')
