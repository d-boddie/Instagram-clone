from django.shortcuts import render
import requests

# Create your views here.

URL = ('https://api.thesneakerdatabase.com/v1/sneakers?limit=98&brand=nike')

def shoes(request):
    try:
        shoe_pic = []
        shoe_image = requests.get(URL).json()
        images = shoe_image["results"]
        for shoe in images:
            if shoe["media"]["smallImageUrl"]:
                shoe_pic.append(shoe["media"]["smallImageUrl"])
        return render(request, "shoes.html", {"shoe_pic": shoe_pic })
    except ConnectionError:
        return render(request, '500.html')

