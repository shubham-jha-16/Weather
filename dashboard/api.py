from django.conf import  settings
import requests



def get_weather_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'    # api
    params = {
        'q': city,
        'appid': settings.OWM_API_KEY,  #api key
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    json_response = response.json()

    weather_data = {
        'temp': json_response['main']['temp'],
        'temp_min': json_response['main']['temp_min'],
        'temp_max': json_response['main']['temp_max'],
        'city': json_response['name'],
        'country': json_response['sys']['country'],
        'lat': json_response['coord']['lat'],
        'lon': json_response['coord']['lon'],
        'weather': json_response['weather'][0]['main'],
        'weather_desc': json_response['weather'][0]['description'],
        'pressure': json_response['main']['pressure'],
        'humidity': json_response['main']['humidity'],
        'wind_speed': json_response['wind']['speed'],
    }
    return weather_data