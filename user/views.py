from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import user

# Create your views here.
def login_page(request):
    if request.method == "POST":
        user= authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        
        if user is not None:
            login(request,user)
            return redirect("/customer")
        else:
            return redirect("/user/login")
    else:
        return render(request, "user/login.html")

def register_page(request):
    print(request.method)
    if request.method == 'POST':
        User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )

        return redirect("/user/login.html")
        print(request.POST)
    else:
        return render(request, "user/register.html")

def logout(request):
    logout(request)
    return redirect("user/login")