from django.shortcuts import render
# to axis the Student from models.py file 
from .models import Student

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
    # varibales like name , email etc take from name attribute from register.html act as key
    n=req.POST.get('name')  
    e=req.POST.get('email')
    c=req.POST.get('contact')
    d=req.POST.get('details')
    i=req.FILES.get('image')
    print(n,e,c,d,i)

    # create query for storing data into the sqlite3 when we register 
    Student.objects.create(Name=n, Email=e, Contact=c, Details=d, Image=i)
    data = Student.objects.all()
    # printing database data on terminal
    # print(data)

    # printing the databse data on html page
    return render(req,'data.html',{'key':data})
