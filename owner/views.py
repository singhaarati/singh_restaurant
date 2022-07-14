import email
from django.shortcuts import render

import user

# Create your views here.
def owner_login(request):
    return render(request,'owner/o_login.html')

def owner_register(request):
    if request.method == 'POST':
        user.objects.create_user(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            password=request

        )
    return render(request,'owner/o_register.html')
