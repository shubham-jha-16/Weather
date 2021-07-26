from django.shortcuts import render, redirect,HttpResponse
from dashboard.models import City
from dashboard.api import get_weather_data
# Create your views here.

def home(request):
    if request.method == 'POST' :
        city = request.POST['city']
        try:
            weather_data = get_weather_data(city)
            p = City(city_name=weather_data["city"])
            p.save()
        except Exception as e:
            weather_data = None

    elif request.method == 'GET' :
        try:
            city = City.objects.latest('date_added').city_name
            weather_data= get_weather_data(city)  # when page get reloaded show the previous searched city data
        except Exception as e :
            weather_data = None
    context = {'weather_data': weather_data}
    return render(request, "home.html", context= context )