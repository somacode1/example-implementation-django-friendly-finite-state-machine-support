from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'state', 'total_price')
    search_fields = ('customer_name', 'customer_email')
