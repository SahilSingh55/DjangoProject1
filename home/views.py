from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context={
        'variable':"this is sent"
    }
    return render(request,"index.html",context)

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")

        else:  
            # No backend authenticated the credentials
            return render(request,'login.html')
        

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        #father = request.POST.get('father')
        #name2 = request.POST.get('name2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        #phone1 = request.POST.get('phone1')
        #MhtcetAppNo = request.POST.get('MhtcetAppNo')
        #MhtcetPercentile = request.POST.get('MhtcetPercentile')
        #MhtcetRank = request.POST.get('MhtcetRank')
        #JeeAppNo = request.POST.get('JeeAppNo')
        #JeePercentile = request.POST.get('JeePercentile')
        #JeeRank = request.POST.get('JeeRank')
        #Address1 = request.POST.get('Address1')
        #Address2 = request.POST.get('Address2')
        #CollegeName = request.POST.get('CollegeName')
        #Percentage = request.POST.get('Percentage')
        #Aadhar = request.POST.get('Aadhar')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")