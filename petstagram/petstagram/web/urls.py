from django.urls import path

from petstagram.web.views import show_home
# NOTE commas are very important
urlpatterns = (
    path('', show_home, name='index'),
)
