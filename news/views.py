from django.shortcuts import render
import requests

url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=017924f89d524708b72d888d6b90c9ad')


def news(request):
    try:
        response = requests.get(url).json()
        posts = response['articles']
        return render(request, 'news.html', {'posts': posts})
    except ConnectionError:
        return render(request, '500.html')