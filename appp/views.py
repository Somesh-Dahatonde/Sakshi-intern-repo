from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fet(request):
    return render(request, 'fet.html')

def home(request):
    return render(request, 'index.html')

def enter(request):
    return render(request, 'enter.html')

def per(request):
    return render(request, 'per.html')

def thn(request):
    return render(request, 'thn.html')