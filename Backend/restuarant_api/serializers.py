from django.db.models import fields
from rest_framework.serializers import ModelSerializer, Serializer
from .models import *


class RestaurantSerializer(ModelSerializer):
    class Meta():
        model = Restuarant
        depth = 2
        fields = ['id', 'name', 'hours']


class OpenDaysSerializer(ModelSerializer):
    class Meta():
        model = OpenDays
        depth = 2
        fields = ['id', 'day_start', 'day_end', 'time_open', 'time_close']
