from django.urls import path
from TFT.champions.views import home

urlpatterns = (
    path('', home),
)
