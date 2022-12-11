from django.shortcuts import render

# Create your views here.

def gallrey(request):
    return render(request, 'gallrey.html')