from django.shortcuts import render
import requests
from datetime import date
from .forms import CovidForm

# Create your views here.

USA = 'https://api.covidactnow.org/v2/states.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc'


def cases(url):
    data = requests.get(url).json()
    total = 0
    for c in data:
        total += c.get('actuals')['cases']
    return total



def deaths(url):
    data = requests.get(url).json()
    total = 0
    for c in data:
        total += c.get('actuals')['deaths']
    return total


def distributed(url):
    data = requests.get(url).json()
    total = 0
    for c in data:
        if c.get('actuals').get('vaccinesDistributed'):
            total += c.get('actuals').get('vaccinesDistributed')
    return total


def administered(url):
    data = requests.get(url).json()
    total = 0
    for c in data:
        if c.get('actuals').get('vaccinesAdministered'):
            total += c.get('actuals').get('vaccinesAdministered')
    return total


def covid(request):
    # form = CovidForm()
    # if request.method == 'POST':
    #     form = CovidForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             data = form.cleaned_data
    #             url = f'https://api.covidactnow.org/v2/state/{data["name"]}.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc'
    #             form = CovidForm()
    #             data = data = {
    #             'cases':cases(url),
    #             'deaths':deaths(url),
    #             'distributed':distributed(url),
    #             'administered':administered(url),
    #             'today': date.today(),
    #             'form': form
    #             }
    #             return render(request, 'covid-19.html', data)
    #         except Exception:
    #             return render(request, '404.html')

    try:
        data = {
            'cases':cases(USA),
            'deaths':deaths(USA),
            'distributed':distributed(USA),
            'administered':administered(USA),
            'today': date.today(),
        }
        return render(request, 'covid-19.html', data)
    except NameError:
        print('NO')

