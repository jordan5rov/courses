from django.shortcuts import render, redirect

from petstagram.web.forms import CreatePetForm
from petstagram.web.helpers import get_profile
from petstagram.web.models import Pet


def pet_actions(request, form_class, success_url, instance, template_name):
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


def create_pet(request):
    return pet_actions(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')


def edit_pet(request):
    return render(request, 'pet_edit.html')


def delete_pet(request):
    return render(request, 'pet_delete.html')
