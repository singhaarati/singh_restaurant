from django.shortcuts import redirect,render
from django.contrib.auth.models import User

# Create your views here.
def login_page(request):
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

        return redirect("/user/login")
        print(request.POST)
    else:
        return render(request, "user/register.html")

# def signout(request):
#     logout(request)
#     messages.success(request,"Logged Out Successfully!")
#     return redirect('home')