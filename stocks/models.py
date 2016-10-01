from django.db import models
    
class Stock(models.Model):
    time= models.FloatField()
    symbol = models.CharField(max_length=100)
    bid = models.DecimalField(max_digits=15, decimal_places=5)
    ask = models.DecimalField(max_digits=15, decimal_places=5)
    exchange = models.IntegerField(default=1)

    class Meta:
        ordering = ['-time']