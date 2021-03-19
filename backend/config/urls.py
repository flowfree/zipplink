"""zipplink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from datetime import datetime
from django.urls import path
from django.http import JsonResponse


def home(request):
    return JsonResponse({'message': 'API is up and running.'})


def server_time(request):
    t = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    return JsonResponse({'server_time': t})


urlpatterns = [
    path('', home, name='home'),
    path('server_time', server_time, name='server_time'),
]
