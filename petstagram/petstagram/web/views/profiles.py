from django.shortcuts import render, redirect

from petstagram.web.forms import ProfileForm
from petstagram.web.models import Pet, PetPhoto
from petstagram.web.helpers import get_profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects \
        .filter(tagged_pets__in=pets) \
        .distinct()

    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        # create form with post
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # create empty form
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    return render(request, 'profile_edit.html')


def delete_profile(request):
    return render(request, 'profile_delete.html')
