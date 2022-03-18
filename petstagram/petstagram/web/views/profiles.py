from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from petstagram.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.web.models import Pet, PetPhoto, Profile
from petstagram.web.helpers import get_profile


# def show_profile(request):
#     profile = get_profile()
#
#     return render(request, 'web/profile_details.html', context)

# we need LoginRequiredMixin in order to get the profile with self.object.user.id
class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'web/profile_details.html'
    object_context_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(user_id=self.object.user.id)
        pet_photos = PetPhoto.objects \
            .filter(tagged_pets__in=pets) \
            .distinct()

        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'pets': pets,
            'is_owner': self.object.user == self.request.user
        })
        return context


def profile_actions(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        # create form with post
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        # create empty form
        form = form_class()
    context = {'form': form}
    return render(request, template_name, context)


def create_profile(request):
    return profile_actions(request, CreateProfileForm, 'index', Profile(), 'web/profile_create.html')


def edit_profile(request):
    return profile_actions(request, EditProfileForm, 'profile', get_profile(), 'web/profile_edit.html')


def delete_profile(request):
    return profile_actions(request, DeleteProfileForm, 'index', get_profile(), 'web/profile_delete.html')
