from django.urls import path
from .views import OrderList, order_detail

urlpatterns = [
    path('orders', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', order_detail, name='order-detail')
]
