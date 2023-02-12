
from rest_framework import serializers
from .models import order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = '__all__'