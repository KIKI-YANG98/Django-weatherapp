from django.shortcuts import render
import requests
from .models import WeatherData
#from .forms import CityForm
#from django_filters import DateRangeFilter,DateFilter

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ef352cf505cf1922ea46b94ae63eb8c2'
    
    msg = "Check the weather of your city"
    msg_class = ""
    error_msg = ""

    if  request.method == 'POST':
        city = request.POST['city']
        city_weather = requests.get(url.format(city)).json()
        if city_weather['cod']==200:
            temperature = city_weather['main']['temp']
            description = city_weather['weather'][0]['description']
            icon = city_weather['weather'][0]['icon']
            data = WeatherData(name=city, temp=temperature, desc=description, icon=icon)
            data.save()
            msg="City Weather data Successfully"
        else:
            error_msg="City is not found"

        if error_msg:
            msg=error_msg
            msg_class="is-danger"

        else:
            msg_class="is-success"
    weather_data = WeatherData.objects.all()

    context = {'weather_data' : weather_data, 'msg': msg, 'msg_class': msg_class}

    return render(request, 'weather/index.html', context)

        
def filter_data(request):
    context = {}
    if  request.method == 'POST':
        city = request.POST['city']
        Date_From = request.POST['Date_From']
        Date_To = request.POST['Date_To']
        weather_data = WeatherData.objects.all()
        date_range = WeatherData.objects.raw('select id, name, date, temp, desc, icon from weather_data where date between "'+Date_From+'" and "'+Date_To+'" and name = "'+city+'"')
        context = {'weather_data' : weather_data, 'date_range' : date_range}
    
        return render(request, 'weather/filterdata.html', context)
    else:
        weather_data = WeatherData.objects.all()
        context = {'weather_data' : weather_data}
        return render(request, 'weather/filterdata.html', context)
