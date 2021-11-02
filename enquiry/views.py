from django.shortcuts import render
from .models import Message
# Create your views here.

def contact(request):
    showbutton = True
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        print(name,email,mobile,message)
        try:
            Message.objects.create(name=name, email=email, mobile=mobile, message=message)
        except Exception as e:
            print('Error: ',e)
            pass
        finally: showbutton = False

    return render(request,'contact.html',{'showbutton':showbutton})
