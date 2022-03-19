from django.urls import path

from petstagram.web.views.generic import DashboardView, HomeView
from petstagram.web.views.pet_photos import PetPhotoDetailsView, like_pet_photo, CreatePetPhotoView, \
    EditPetPhotoView
from petstagram.web.views.pets import CreatePetView, EditPetView, DeletePetView

# NOTE commas are very important
urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='create photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit pet photo'),
)
