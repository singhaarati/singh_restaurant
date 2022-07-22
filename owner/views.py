import email
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
import owner
from owner.models import Owner
from owner.form import OwnerForms

import user

# Create your views here.
def index(request):
    items=Owner.objects.all()
    return render(request,"owner/owner.html",{'owner': owner})

def owner_login(request):
    if request.method == "POST":
        user= authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/owner/o_login")
    else:    
            return render(request,'owner/o_login.html')

def owner_register(request):
    print(request.method)
    if request.method == 'POST':
        User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        return redirect("/owner/o_login")
        print(request.POST)
    else:
        return render(request,'owner/o_register.html')

def owner_post(request):
    return render(request,'owner/owner.html')


def save(request):
    print(request.FILES)
    form=OwnerForms(request.POST,)
    form.save()

    return redirect("/owner")

