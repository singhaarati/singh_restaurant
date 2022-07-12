from django.shortcuts import render

import customer
from customer.models import Customer

# Create your views here.
def index (request):
    return render (request,'customer/index.html')
