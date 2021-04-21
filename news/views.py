from django.shortcuts import render
import requests

import os

from dotenv import load_dotenv
load_dotenv()

# Create your views here.

API_KEY = os.getenv(
    'NEWS_API_KEY'
    )

url = (f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}')


def news(request):
    try:
        response = requests.get(url).json()
        posts = response['articles']
        return render(request, 'news.html', {'posts': posts})
    except ConnectionError:
        return render(request, '500.html')