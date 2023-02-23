from django.db import models
from django_fsm import FSMField, transition

class Order(models.Model):
    """
    In this example, we define a Order model with a state field that is implemented as a FSMField from Django-FSM.
    The state field is initialized with a default value of 'new', and has several possible choices defined by the STATE_CHOICES list.

    We define several transition methods using the @transition decorator from Django-FSM.
    Each transition method has a field parameter that specifies the name of the field to update (in this case, state), and source and target parameters that define the starting and ending states of the transition.
    For example, the start_processing method can only be called when the order is in the 'new' state, and transitions the order to the 'processing' state.

    Each transition method is currently implemented with basic logic.
    You would need to replace the statements with actual code to implement the desired behavior of the transition.

    To use this Order model in your Django application, you would need to define a corresponding serializer and view class in Django Rest Framework that leverages Django-FSM to implement the appropriate state transitions.

    Author: philipmutua@duck.com
    """
    state = FSMField(default='new')
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    """
    source parameter accepts a list of states, or an individual state or django_fsm.State implementation.

    You can use * for source to allow switching to target from any state.

    You can use + for source to allow switching to target from any state excluding target state.

    docs: https://github.com/viewflow/django-fsm
    """
    @transition(field=state, source='new', target='processing')
    def start_processing(self):
        # replace the code with your logic here
        return "Order processing.....!"

    @transition(field=state, source='*', target='shipped')
    def complete_processing(self):
        # replace the code with your logic here
        return "Order shipped......"

    @transition(field=state, source=['*', 'processing'], target='cancelled')
    def cancel(self):
        # replace the code with your logic here
        return 'Order cancelled .........'
