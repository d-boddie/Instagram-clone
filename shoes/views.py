from django.shortcuts import render
import requests

# Create your views here.

URL = ('https://api.thesneakerdatabase.dev/v2/sneakers?limit=100&brand=nike')

def shoes(request):
    try:
        shoe_pic = []
        shoe_image = requests.get(URL).json()
        images = shoe_image["results"]
        for shoe in images:
            if shoe["image"]["small"]:
                shoe_pic.append(shoe["image"]["small"])
        return render(request, "shoes.html", {"shoe_pic": shoe_pic })
    except ConnectionError:
        return render(request, '500.html')

