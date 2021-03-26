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
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers

from apps.urlshortener.views import URLViewSet, redirect_short_url


router = routers.SimpleRouter(trailing_slash=False)
router.register('urls', URLViewSet)

urlpatterns = router.urls + [
    path('', TemplateView.as_view(template_name='urlshortener/index.html'), name='urlshortener'),
    path('<slug:slug>', redirect_short_url, name='redirect_short_url'),
]


def handle404(request, exception):
    return render(request, '404.html', status=404)


handler404 = handle404
