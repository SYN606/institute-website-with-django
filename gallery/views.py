from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def gallery(request):
    return render(request, "gallery.html")

