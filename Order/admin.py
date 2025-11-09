from django.contrib import admin
from .models import TableBooking


class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'order_time', 'people_count']
    list_filter = ['order_time']
    search_fields = ['name', 'phone', 'email']


admin.site.register(TableBooking, TableAdmin),
