import email
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
import owner
from owner.models import Owner
from owner.form import OwnerForms

import user

# Create your views here.
def index(request):
    items=Owner.objects.all()
    return render(request,"owner/owner.html",{'owner': owner})

def owner_login(request):
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

# def create(request):
#     return render(request,"owner/owner.html")

def save(request):
    print(request.FILES)
    form=OwnerForms(request.POST,request.FILES)
    form.save()

    return redirect("/owner")