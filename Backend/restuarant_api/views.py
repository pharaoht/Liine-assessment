from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
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


@api_view(['POST'])
def add_hours(request):
    error = Response(data={'no data': 'The data you requested can not be found'},
                     status=status.HTTP_400_BAD_REQUEST)

    try:
        start_day = Day.objects.get(day_value=request.data['day_start'])
        end_day = Day.objects.get(day_value=request.data['day_end'])
        days = OpenDays(day_start=start_day, day_end=end_day)

    except:
        print("ERROR")
        return error

    serializer = OpenDaysSerializer(
        days, data=request.data)

    if serializer.is_valid():
        serializer.save()
        http201 = create_restaurant(serializer, request.data, error)
        return http201

    else:
        print("error")
        return error


def create_restaurant(serializer, post_data, error):
    rest_serializer = RestaurantSerializer(data=post_data)

    if rest_serializer.is_valid():
        rest_serializer.save()
        restaurantId = rest_serializer.data['id']
        restuarant = Restuarant.objects.get(id=restaurantId)
        hours = OpenDays.objects.get(id=serializer.data['id'])
        restuarant.hours.add(hours)

        return Response(data={"good": "Created"}, status=status.HTTP_201_CREATED)
    else:
        return error


def date_conversion(date):
    x = date[0].split('/')
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    new_date = datetime.datetime(year, month, day)
    return new_date.strftime("%w")
