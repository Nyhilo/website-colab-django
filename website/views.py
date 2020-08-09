from django.http import HttpResponse

def index(request):
     return HttpResponse("Hello, world")

def demo(request):
     return HttpResponse("This is a test")