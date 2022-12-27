from django.shortcuts import render


def nielit(request):
    return render(request, 'n-courses.html')

def icai(request):
    return render(request, 'i-courses.html')

def short_term(request):
    return render(request, 'st-courses.html')

# nielit courses views |>
def olevel(request):
    return render(request, 'o-level.html')

def ccc(request):
    return render(request, 'ccc.html')

def ccc_plus(request):
    return render(request, 'ccc-plus.html')

def adca(request):
    return render(request, 'adca.html')

def eca(request):
    return render(request, 'eca.html')

# icai courses views

def cat(request):
    return render(request, 'cat.html')

def tally(request):
    return render(request, 'tally.html')