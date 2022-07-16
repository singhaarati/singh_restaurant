import email
from django.contrib.auth.models import User
from django.shortcuts import redirect,render

import user

# Create your views here.
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
