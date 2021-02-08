from django.db import models

# Create your models here.
class WeatherModel(models.Model):
    region = models.CharField(max_length=50)
    req_date = models.DateTimeField(auto_now_add=True)
    temp_high = models.DecimalField(max_digits=3, decimal_places=1)
    temp_low = models.DecimalField(max_digits=3, decimal_places=1)
    rain_prob = models.DecimalField(max_digits=3, decimal_places=1)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.region + ',' + self.req_date