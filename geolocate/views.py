from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/73.48.150.2?access_key=e63c80c85f6b1893fd3938a03264cb71')
    geodata = response.json()
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })