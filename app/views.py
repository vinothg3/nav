from django.shortcuts import render

# Create your views here.
def fornt(request):
    return render(request,'fornt.html')
def home1(request):
    return render(request,'home1.html')
def log(request):
    return render(request,'log.html')
def reg(request):
    return render(request,'reg.html')