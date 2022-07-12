from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

# def about(request):
#     return render(request,'home/about.html')

def dash(request):
    return render(request,'dash_layout.html')
