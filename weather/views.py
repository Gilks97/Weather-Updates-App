import requests
import os
from django.shortcuts import render
from datetime import datetime, timezone, timedelta

def get_weather_theme(condition, icon):
    condition = condition.lower()
    is_night = icon.endswith('n')

    if 'thunderstorm' in condition:
        return 'thunderstorm'
    elif 'drizzle' in condition or 'rain' in condition:
        return 'rain-night' if is_night else 'rain'
    elif 'snow' in condition:
        return 'snow-night' if is_night else 'snow'
    elif 'mist' in condition or 'fog' in condition or 'haze' in condition:
        return 'mist-night' if is_night else 'mist'
    elif 'cloud' in condition:
        return 'cloudy-night' if is_night else 'cloudy'
    elif 'clear' in condition:
        return 'night' if is_night else 'sunny'
    else:
        return 'default'


def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = os.getenv('WEATHER_API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            utc_offset_seconds = data['timezone']
            city_timezone = timezone(timedelta(seconds=utc_offset_seconds))
            city_time = datetime.now(tz=city_timezone)

            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon'] 

            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': description.capitalize(),
                'icon': data['weather'][0]['icon'],
                'date': city_time.strftime('%A, %d %B %Y'),
                'time': city_time.strftime('%I:%M %p'),
                'theme': get_weather_theme(description, icon),
            }
        else:
            error = "City not found. Please try again."

    return render(request, 'weather/index.html', { 
        'weather': weather_data,
        'error': error,
    })