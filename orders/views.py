from django.views.generic import ListView
from .models import Order

class OrderHistoryView(ListView):
    model = Order
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cars.models import Car
from .models import Order

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
    return redirect('order_history')

from django.urls import path
from .views import OrderHistoryView, buy_car

urlpatterns = [
    path('history/', OrderHistoryView.as_view(), name='order_history'),
    path('buy/<int:car_id>/', buy_car, name='buy_car'),
]