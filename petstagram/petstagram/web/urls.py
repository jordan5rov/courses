from django.urls import path

from petstagram.web.views.generic import show_dashboard, show_home
from petstagram.web.views.pet_photos import show_pet_photo_details, like_pet_photo, create_pet_photo, edit_pet_photo
from petstagram.web.views.pets import create_pet, edit_pet, delete_pet
from petstagram.web.views.profiles import show_profile, create_profile, edit_profile, delete_profile

# NOTE commas are very important
urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/create/', create_pet, name='create pet'),
    path('pet/add/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', create_pet_photo, name='create photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
)
