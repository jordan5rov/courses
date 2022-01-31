from django.urls import path
from TFT.landing_page.views import landing_page


urlpatterns = (
    path('', landing_page),
)
