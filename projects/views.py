from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def allprojects(request):
    projects = Project.objects.all().order_by('-id')
    return render(request,'projects.html',{'projects':projects})


def project_detail(request):
    project = Project.objects.get(id=int(request.GET.get('id')))
    response = {
        'name': project.name,
        'client': project.client,
        'buildup_area': project.buildup_area,
        'location': project.location,
        'content': project.content,
        'images': [i.image.url for i in project.images()],
    }
    return JsonResponse(response)
