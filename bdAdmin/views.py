from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def introduce_world(request):
    return HttpResponse("Hello World !")