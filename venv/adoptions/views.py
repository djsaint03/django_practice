from django.shortcuts import render

from django.http import HttpResponse,Http404
from django.views.generic import ListView


from .models import Pet,Humans

# Create your views here.

def home(request):
    pets = Pet.objects.all()
    return render(request, "home.html",{"pets":pets,})


def pet_details(request, pet_id):
    try:
        pet = Pet.objects.get(id = pet_id)

    except Pet.DoesNotExist:
        raise Http404("pet not found")
    return render(request, "pet_details.html", {"pet":pet,})

