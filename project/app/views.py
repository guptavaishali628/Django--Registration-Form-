from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req, 'landing.html')

def register(req):
    return render(req, 'register.html')

def registerData(req):
    print(req.method)
    print(req.POST)
