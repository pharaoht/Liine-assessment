from django.db import models


class Day(models.Model):
    day_value = models.IntegerField()
    day_name = models.CharField(max_length=255)

    def __str__(self):
        return self.day_name


class OpenDays(models.Model):
    day_start = models.ForeignKey(
        Day, related_name='start_day', on_delete=models.CASCADE)
    day_end = models.ForeignKey(
        Day, related_name='end_day', on_delete=models.CASCADE)
    time_open = models.CharField(max_length=255)
    time_close = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.day_start} to {self.day_end}: {self.time_open}-{self.time_close}"


class Restuarant(models.Model):
    name = models.CharField(max_length=255)
    hours = models.ManyToManyField(
        OpenDays, related_name='hours_opened', blank=False)

    def hours_opened(self):
        return ",".join([str(p) for p in self.hours.all()])

    def __str__(self):
        return self.name
