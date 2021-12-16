from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import *


class RestaurantSerializer(ModelSerializer):
    class Meta():
        model = Restuarant
        depth = 2
        fields = ['id', 'name', 'hours']
