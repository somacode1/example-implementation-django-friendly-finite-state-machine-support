from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django_fsm import can_proceed
from .models import Order
from .serializers import OrderSerializer


"""
Example API view

URL to update order detail state
================================================================

http://127.0.0.1:9008/orders_api/order/2/

Expected JSON
================================================================

{
"order_state": "cancelled",

}

In this example, we define a view called order_detail that takes a primary key (pk) as a parameter.
We retrieve the Order object using get_object_or_404.

and call the appropriate transition method on the Order object.

Finally, we render the  serialized Order object
"""
@api_view(['GET', 'POST'])
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.data.get('order_state') == 'processing':
        order.start_processing()
        # do some logic here
    elif request.data.get('order_state') == 'shipped':
         # do some logic here
        order.complete_processing()
    elif  request.data.get('order_state') == 'cancelled':
         # do some logic here
        order.cancel()

    else:
        # not required though
        pass
    serializer = OrderSerializer(order)
    return Response(serializer.data)



class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

