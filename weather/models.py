from django.db import models
from datetime import datetime
#from django_filters import DateRangeFilter,DateFilter

class WeatherData(models.Model):

    name = models.CharField(max_length=25)
    
    date = models.DateField(default=datetime.now(), blank=True)

    temp = models.FloatField()

    desc = models.CharField(max_length=200)

    icon = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    
    class Meta:
        db_table = "weather_data"
    
    def __str__(self): #show the actual city name on the dashboard
        return self.name