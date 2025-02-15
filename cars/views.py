from django.views.generic import ListView, DetailView
from .models import Car, Brand

class HomeView(ListView):
    model = Car
    template_name = 'cars/home.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

from django.shortcuts import get_object_or_404, redirect
from .models import Car, Comment

def add_comment(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        Comment.objects.create(car=car, name=name, comment=comment_text)
    return redirect('car_detail', car_id=car_id)

from django.urls import path
from .views import HomeView, CarDetailView, add_comment

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:car_id>/comment/', add_comment, name='add_comment'),
]