from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def gallery(request):

    image = Gallery.objects.all()
    context = {'image' : image}
    return render(request, "gallery.html", context)

