from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def demo(request):
    return HttpResponse("This is a test")
   
def test(request):
    return HttpResponse("To... um... ah")
