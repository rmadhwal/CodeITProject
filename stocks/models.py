from django.db import models
    
class Stock(models.Model):
    time= models.FloatField()
    symbol = models.CharField(max_length=100)
    bid = models.FloatField()
    ask = models.FloatField()
    exchange = models.IntegerField(default=1)

    class Meta:
        ordering = ['-time']