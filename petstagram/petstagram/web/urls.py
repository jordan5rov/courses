from django.urls import path

from petstagram.web.views.generic import DashboardView, HomeView
from petstagram.web.views.pet_photos import show_pet_photo_details, like_pet_photo, create_pet_photo, edit_pet_photo
from petstagram.web.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.web.views.profiles import show_profile, create_profile, edit_profile, delete_profile

# NOTE commas are very important
urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/create/', CreatePetView.as_view(), name='create pet'),
    path('pet/add/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', create_pet_photo, name='create photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
)
