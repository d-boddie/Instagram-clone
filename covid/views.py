from django.shortcuts import render
import requests
from datetime import date
from .forms import CovidForm
import os

from dotenv import load_dotenv
load_dotenv()

# Create your views here.

API_KEY = os.getenv(
    'COVID_API_KEY'
    )

USA = f"https://api.covidactnow.org/v2/states.json?apiKey={API_KEY}"


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

