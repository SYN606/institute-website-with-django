from django.shortcuts import render


def nielit(request):
    return render(request, 'n-courses.html')

def icai(request):
    return render(request, 'i-courses.html')

def short_term(request):
    return render(request, 'st-courses.html')