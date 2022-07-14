from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def buy_page(request):
    return render(request,'home/buy.html')
