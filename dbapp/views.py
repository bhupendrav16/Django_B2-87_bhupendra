from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render( request, 'home/home.html')

def about(request):
    return render( request, 'home/about.html')

def contact( request):
    book  =Book.objects.all()
    return render( request, 'home/contact.html', {'book':book})
