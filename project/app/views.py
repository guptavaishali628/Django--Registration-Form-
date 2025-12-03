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

def stu_data(req):
    # # fetch all data from database:
    # data = Student.objects.all() 
    # # printing database data on terminal
    # print(data)

    # # applying filter on data with multiple columns:
    # data = Student.objects.filter(Name='Vaishali gupta', Contact=8976645640)
    # print(data)

    # # method to return all object exclude Stuti
    # data= Student.objects.exclude(Name='Stuti Dubey')
    # print(data)

    # # method to arrange data acc to you using order_by bydefault it order data by id
    # # data= Student.objects.order_by('Name')
    # # converting in descending order using (-) operator
    # data = Student.objects.order_by('-Name') 
    # print(data)

    # # method to {reverse()} reverse data
    # data1=Student.objects.order_by('-Name')
    # data=data1.reverse()
    # print(data)

    # method to return data first five students using slice method:
    # data=Student.objects.all()[:5]
    # method to return data last five students using slice method by using reverse() function:
    # data=Student.objects.all()[-1:-5] do not support negative indexing
    data=(Student.objects.all()).reverse()[:5]


    # printing the databse data on html page
    return render(req,'data.html',{'key':data})
