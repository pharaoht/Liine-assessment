from django.test import TestCase
from .models import Day, OpenDays, Restuarant


class URLTests(TestCase):

    def test_get_restaurants(self):
        response = self.client.get('/api/get-restaurants-opened/')
        self.assertEqual(response.status_code, 200)


class TestAppModels(TestCase):

    def test_table_day_str(self):
        day = Day.objects.create(day_name="Tuesday", day_value=2)
        self.assertEqual(str(day), 'Tuesday')

    def test_table_opendays_str(self):
        day_1 = Day.objects.create(day_name="Tuesday", day_value=2)
        day_2 = Day.objects.create(day_name="Monday", day_value=1)
        hours = OpenDays.objects.create(
            day_start=day_2, day_end=day_1, time_open='10:00:00', time_close='12:00:00')
        self.assertEqual(str(hours), 'Monday to Tuesday: 10:00:00-12:00:00')

    def test_table_restaurant_hours_open(self):
        rest = Restuarant.objects.create(name="Test Restaurant")

        self.assertEqual(str(rest.name), 'Test Restaurant')

    def test_mtm_str(self):
        day_1 = Day.objects.create(day_name="Tuesday", day_value=2)
        day_2 = Day.objects.create(day_name="Monday", day_value=1)
        hours = OpenDays.objects.create(
            day_start=day_2, day_end=day_1, time_open='10:00:00', time_close='12:00:00')

        rest = Restuarant.objects.create(name="Test Restaurant")
        rest.hours.set([hours.id])
        self.assertEqual(",".join([str(p) for p in rest.hours.all()]),
                         "Monday to Tuesday: 10:00:00-12:00:00")


class TestAppViews(TestCase):

    def test_split_date(self):
        date = '2021/12/16_10:00:00'
        new_date = date.split("_")
        self.assertEqual(new_date, ['2021/12/16', '10:00:00'])
