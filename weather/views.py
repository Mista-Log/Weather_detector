from django.shortcuts import render
import json
import urllib

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        gen = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=63e57e1385aa6272e3e23d9d8727c4d6').read()
        json_data = json.loads(gen)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }

    else:
        city = ' '
        data ={}
    return render(request, 'index.html', {'city': city, 'data': data})