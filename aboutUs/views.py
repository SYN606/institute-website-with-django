from django.shortcuts import render

# Create your views here.

def aboutIns(request):
    return render(request, 'aboutIns.html')

def FacPro(request):
    return render(request, 'FacPro.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')