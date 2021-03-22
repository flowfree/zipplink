from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets
from .models import URL
from .serializers import URLSerializer


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


def redirect_short_url(request, slug):
    url = get_object_or_404(URL, slug=slug)
    return redirect(url.long_url)
