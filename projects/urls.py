from django.urls import path
from .views import *

urlpatterns = [
    path('all',allprojects,name = 'projects'),
    path('fetch',project_detail,name='fetchproject')
]
