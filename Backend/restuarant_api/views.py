from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
import datetime


@api_view(['GET'])
@permission_classes([])
def get_restaurants(request):
    try:
        dateRequested = request.query_params['dateRequested']
        split_date = dateRequested.split('_')
        weekday = date_conversion(split_date)
        time = split_date[1]

        restaurants = Restuarant.objects.filter(
            hours__day_start__day_value__lte=weekday, hours__day_end__day_value__gte=weekday, hours__time_open__lte=time, hours__time_close__gte=time)

        serializer = RestaurantSerializer(restaurants, many=True)

    except:
        return Response({'no data': 'The data you requested can not be found'})

    return Response({'message': serializer.data})


def date_conversion(date):
    x = date[0].split('/')
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    new_date = datetime.datetime(year, month, day)
    return new_date.strftime("%w")
