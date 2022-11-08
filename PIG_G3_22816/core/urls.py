from django.urls import path
from .views import HomePageView, EjemploPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('ejemplo/', EjemploPageView.as_view(), name="ejemplo"),
]