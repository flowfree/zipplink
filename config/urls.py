"""urlshortener URL Configuration

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
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers

from apps.urlshortener.views import URLViewSet, redirect_short_url


@api_view()
def home(request):
    return Response({'message': 'API is up and running.'})


@api_view()
def server_time(request):
    t = datetime.now()
    return Response({'server_time': t.strftime('%Y-%m-%dT%H:%M:%SZ')})


router = routers.SimpleRouter(trailing_slash=False)
router.register('urls', URLViewSet)

urlpatterns = router.urls + [
    path('', home),
    path('server_time', server_time),
    path('<slug:slug>', redirect_short_url),
]
