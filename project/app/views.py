from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req, 'landing.html')

def register(req):
    return render(req, 'register.html')

def registerData(req):
    print(req.method)
    print(req.POST)
    print(req.GET)
    print(req.FILES)
    # printing data from dictionary
    n=req.POST.get('name')  
    e=req.POST.get('email')
    c=req.POST.get('contact')
    d=req.POST.get('details')
    image=req.FILES.get('image')
    print(n,e,c,d,image)
