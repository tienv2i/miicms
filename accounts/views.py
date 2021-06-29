from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index page')

def login(request):
    return HttpResponse('Login page')

def logout(request):
    return HttpResponse('logout page')

def register(request):
    return HttpResponse('Register page')
