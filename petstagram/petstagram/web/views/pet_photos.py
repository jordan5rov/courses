from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.web.models import PetPhoto


# def show_pet_photo_details(request, pk):
#     # pet_photo = PetPhoto.objects.get(id=pk)
#     pet_photo = PetPhoto.objects \
#         .prefetch_related('tagged_pets') \
#         .get(pk=pk)
#
#     context = {
#         'pet_photo': pet_photo,
#     }
#
#     return render(request, 'web/photo_details.html', context)


class PetPhotoDetailsView(views.DetailView):
    model = PetPhoto
    template_name = 'web/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset


class CreatePetPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = PetPhoto
    template_name = 'web/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def like_pet_photo(request, pk):
    # like the pet photo
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)


# def create_pet_photo(request):
#     return render(request, 'web/photo_create.html')


def edit_pet_photo(request):
    return render(request, 'web/photo_edit.html')
