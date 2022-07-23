from tkinter import EW
from django.shortcuts import redirect, render
from customer.form import CustomerForms

from customer.models import Customer

# Create your views here.
def index(request):
    customer = Customer.objects.all()
    return render(request,'customer/index.html',{'customer': customer})


def create(request):
    return render(request, "customer/create.html")

def saveFn(request):
    print(request.FILES)
    form=CustomerForms(request.POST,request.FILES)
    form.save()

    return  redirect("/customer")

def edit(request,id):
    print(id)
    data=Customer.objects.get(id=id)
    return render(request,"customer/edit.html",{'data':data})

def update(request,id):
    data=Customer.objects.get(id=id)
    form=CustomerForms(request.POST,request.FILES, instance=data)
    form.save()
    return redirect("/customer")

def delete(request,id):
    data=Customer.objects.get(id=id)
    data.delete()
    return redirect("/customer")