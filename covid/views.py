from django.shortcuts import render
import requests
from datetime import date

# Create your views here.


def cases():
    data = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc').json()
    total = 0
    for c in data:
        total += c.get('actuals')['cases']
    return total


def deaths():
    data = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc').json()
    total = 0
    for c in data:
        total += c.get('actuals')['deaths']
    return total


def distributed():
    data = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc').json()
    total = 0
    for c in data:
        if c.get('actuals').get('vaccinesDistributed'):
            total += c.get('actuals').get('vaccinesDistributed')
    return total


def administered():
    data = requests.get('https://api.covidactnow.org/v2/states.json?apiKey=b7d6859963484ce1aa74581ae7f5d8cc').json()
    total = 0
    for c in data:
        if c.get('actuals').get('vaccinesAdministered'):
            total += c.get('actuals').get('vaccinesAdministered')
    return total


def covid(request):
    try:
        data = {
            'cases':cases(),
            'deaths':deaths(),
            'distributed':distributed(),
            'administered':administered(),
            'today': date.today()
        }
        return render(request, 'covid-19.html', data)
    except NameError:
        print('NO')