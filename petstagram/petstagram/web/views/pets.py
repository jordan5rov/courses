from django.urls import reverse_lazy
from django.views import generic as views
from petstagram.web.forms import CreatePetForm, EditPetForm, DeletePetForm


# def pet_actions(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         # create form with post
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         # create empty form
#         form = form_class()
#     context = {
#         'form': form,
#         'pet': instance
#     }
#     return render(request, template_name, context)
#
#
# def create_pet(request):
#     return pet_actions(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'web/pet_create.html')
#
#
# def edit_pet(request, pk):
#     return pet_actions(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'web/pet_edit.html')
#
#
# def delete_pet(request, pk):
#     return pet_actions(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'web/pet_delete.html')
class CreatePetView(views.CreateView):
    template_name = 'web/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    # if form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    template_name = 'web/pet_edit.html'
    form_class = EditPetForm


class DeletePetView(views.DeleteView):
    template_name = 'web/pet_delete.html'
    form_class = DeletePetForm
