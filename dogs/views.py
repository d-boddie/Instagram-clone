from django.shortcuts import render
import requests
# Create your views here.

URL = 'https://dog.ceo/api/breeds/image/random/50'

def dogs(request):
    try:
        dogs_image = requests.get(URL).json()
        images = dogs_image.get('message')
        return render(request, 'dogs.html', {'images':images})
    except ConnectionError:
        return render(request, '500.html')







