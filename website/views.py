from django.http import HttpResponse

def index(request):
     return HttpResponse("Hello, world")

def test(request):
     return HttpResponse("To... um... ah")