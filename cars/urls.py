from django.urls import path
from .views import HomeView, CarDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]