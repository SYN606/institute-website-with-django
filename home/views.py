from django.shortcuts import render
from django.http import HttpResponse

from .models import User

def index(request):
    return render(request, 'index.html')


def contact(request):

    if request.method == "POST":

        name = request.POST["name"]
        ph_number = request.POST["ph_number"]
        email = request.POST["email"]
        query = request.POST["query"]

        user_query = User(
            name = name,
            ph_number = ph_number,
            email = email,
            query = query
        )

        user_query.save()
        return HttpResponse("Query uploaded successfully")
    
    else:
        return render(request, 'contact.html')