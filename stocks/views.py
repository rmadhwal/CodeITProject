from .models import Stock
from serializers import StockSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StockList(APIView):
    """
    List all stocks, or push stocks in.
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

class StockDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
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
        num = 0
        while stock.exists():
            stock[num].delete()
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
        url = 'http://cis2016-exchange1.herokuapp.com/api/market_data'
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        for num in range(0, len(data)):
            serializer = StockSerializer(data=data[num])
            if serializer.is_valid():
                serializer.save()
        return Response(data)

    def post(self, request, format=None):
        for num in range(0, len(request.data)-1):
            serializer = StockSerializer(data=request.data[num])
            if serializer.is_valid():
                serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

        
        
    