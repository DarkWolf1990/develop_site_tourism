from django.shortcuts import render
from .models import Accommodation

def main(request):
    return render(request, 'mainapp/index.html')

def accommodations(request):
    title = 'размещение'
    list_of_accommodations = Accommodation.objects.filter(is_active=True)
    content = {
        'title':title,
        'list_of_accommodations':list_of_accommodations,
    }
    return render(request, 'mainapp/accommodations.html')
