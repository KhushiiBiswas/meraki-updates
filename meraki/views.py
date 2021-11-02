from django.shortcuts import render

def home(request):
    return render(request,'index.html')



def temp(request):
    return render(request,'temp.html')
