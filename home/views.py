from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is Sample page for Deploy!!!")
