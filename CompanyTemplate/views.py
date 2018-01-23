from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def model1(request):
    return render(request,'./Model1/base.html')
