from rest_framework import serializers
from stocks.models import Stock


class IndStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('time', 'symbol', 'bid', 'ask')

    def create(self, validated_data):
        """
        Create and return a new `Stock` instance, given the validated data.
        """
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.time = validated_data.get('time', instance.time)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.bid = validated_data.get('bid', instance.bid)
        instance.ask = validated_data.get('ask', instance.ask)
        instance.save()
        return instance