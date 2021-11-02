from django.shortcuts import render
from .models import *
# Create your views here.

def members(request):
    team = Member.objects.all()
    return render(request, 'studio.html', {'team' : team})


