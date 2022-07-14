from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def buy_page(request):
    
        if  request.method == "POST":
            firstname= request.POST.get('firstname')
            lastname= request.POST.get('lastname')
            username= request.POST.get('username')
            email= request.POST.get('email')
            mobile= request.POST.get('mobile')
            address= request.POST.get('address')
            zipcode= request.POST.get('zipcode')
            buy = buy(firstname=firstname, lastname=lastname, username=username, email=email, mobile=mobile, address=address, zipcode=zipcode)
            buy.save()
            
        return render(request, 'home/buy.html')  
