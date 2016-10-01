from .models import Stock
from serializers import StockSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StockList(APIView):
    """
    List of aggregated stocks data - This is nasty, try cutting down on the data you need by customizing the url.
    Add a /*symbol number*/ to the url to get a list of quotations of only one symbol
    Add a /exchange/*exchange number*/ to the url to get a list of quotations of only a certain exchange (1,2 or 3)
    Add a /*symbol number*/latest/ to the url to get only the latest stock for a certain symbol
    Add a /exchange/*exchange number*/*symbol number* to the url to get a certain stock for a certain exchange
    OR
    To see the datasets that we will we working on:
    Add a /exchange/*exchange number*/*symbol number*/100 to the url
    
    Our secret now that you have stumbled upon it: Is to calculate a statistic based on the last 100 quotations of each individual stock in each individual exchange:
    And to buy the stock with the best statistic.
    """
    def get(self, request, format=None):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        for num in range(0, len(request.data)-1):
            serializer = StockSerializer(data=request.data[num])
            if serializer.is_valid():
                serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, format=None):
        stock = Stock.objects.all()
        num = 0
        while stock.exists():
            stock[num].delete()
            stock = Stock.objects.all()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExchangeDetail(APIView):
    """
    Quotations of a specific exchange
    """
    def get_object(self, pk):
        try:
            stock = Stock.objects.filter(exchange=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = Stock.objects.filter(exchange=pk)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        stock = Stock.objects.filter(exchange=pk)
        num = 0
        while stock.exists():
            stock[num].delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StockDetail(APIView):
    """
    Quotations of a specific stock (Through all 3 exchanges)
    """
    def get_object(self, pk):
        try:
            stock = Stock.objects.filter(symbol=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = Stock.objects.filter(symbol=pk)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        stock = Stock.objects.filter(symbol=pk)
        while stock.exists():
            stock[0].delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExchangeStockDetail(APIView):
    """
    Quotation of a specific Exchange stock
    """
    def get_object(self, pk):
        try:
            stock = Stock.objects.filter(exchange=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, pk2, format=None):
        stock = Stock.objects.filter(exchange=pk).filter(symbol=pk2)
        while len(stock) > 50:
            stock[50].delete()
            stock = Stock.objects.filter(exchange=pk).filter(symbol=pk2)
        stock = Stock.objects.filter(exchange=pk).filter(symbol=pk2)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        stock = Stock.objects.filter(symbol=pk)
        num = 0
        while stock.exists():
            stock[num].delete()
            stock = Stock.objects.filter(symbol=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StockLatest(APIView):
    def get(self, request, pk, format=None):
        stock = Stock.objects.filter(symbol=pk)[0]
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        stock = Stock.objects.filter(symbol=pk)[0]
        stock.delete()
        return Response(status=204)
    
class StockRefresh(APIView):
    def get(self, request, format=None):
        import urllib2
        import json
        
        """
        Exchange 1 Patch
        """
        
        url = 'http://cis2016-exchange1.herokuapp.com/api/market_data'
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        exchange1 = {'exchange' : 1}
        for num in range(0, len(data)):
            newdata = dict(data[num].items()+exchange1.items())
            serializer = StockSerializer(data=newdata)
            if serializer.is_valid():
                serializer.save()
                
                
        """
        Exchange 2 Patch
        """
        url = 'http://cis2016-exchange2.herokuapp.com/api/market_data'
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        exchange2 = {'exchange' : 2}
        for num in range(0, len(data)):
            newdata = dict(data[num].items()+exchange2.items())
            serializer = StockSerializer(data=newdata)
            if serializer.is_valid():
                serializer.save()
                
        """
        Exchange 3 Patch
        """
        url = 'http://cis2016-exchange3.herokuapp.com/api/market_data'
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        exchange3 = {'exchange' : 3}
        for num in range(0, len(data)):
            newdata = dict(data[num].items()+exchange3.items())
            serializer = StockSerializer(data=newdata)
            if serializer.is_valid():
                serializer.save()
                
                
        return Response(data)

    def post(self, request, format=None):
        for num in range(0, len(request.data)-1):
            serializer = StockSerializer(data=request.data[num])
            if serializer.is_valid():
                serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

        
        
    