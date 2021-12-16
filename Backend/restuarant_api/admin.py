from django.contrib import admin
from .models import Restuarant, OpenDays, Day


class RestuarantCustom(admin.ModelAdmin):
    list_display = ('name', 'hours_opened')
    list_filter = ('name',)


admin.site.register(Day)
admin.site.register(Restuarant, RestuarantCustom)
admin.site.register(OpenDays)
