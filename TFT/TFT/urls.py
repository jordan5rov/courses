from django.contrib import admin
from django.urls import path, include


urlpatterns = (
    path('', include('TFT.landing_page.urls')),
    path('admin/', admin.site.urls),
    path('champions/', include('TFT.champions.urls')),
)
