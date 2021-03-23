"""zipplink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('ZippLink is under development. Please come back soon!')
    
    
def greet(request, name):
    return HttpResponse(f'Hello, {name.title()}!')


urlpatterns = [
    path('', home, name='home'),
    path('greet/<slug:name>', greet, name='greet'),
]
