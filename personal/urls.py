from django.urls import path
from .views import HomePageView, CalculatorPageView, JSObjectPageView


urlpatterns = [
	path('calculator/', CalculatorPageView.as_view(), name='calculator'),
	path('jsObjects/', JSObjectPageView.as_view(), name='jsObjects'),
	path('', HomePageView.as_view(), name='home')
]