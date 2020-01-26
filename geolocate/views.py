from django.conf import settings
from django.shortcuts import render


# Create your views here.
import requests

def home(request):
    response = requests.get(f'http://api.ipstack.com/73.48.150.2?access_key={settings.ACCESS_KEY}')
    geodata = response.json()
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })