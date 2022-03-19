# def show_profile(request):
#     profile = get_profile()
#
#     return render(request, 'web/profile_details.html', context)

# we need LoginRequiredMixin in order to get the profile with self.object.user.id

#
#
# def profile_actions(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         # create form with post
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         # create empty form
#         form = form_class()
#     context = {'form': form}
#     return render(request, template_name, context)
#
#
# def create_profile(request):
#     return profile_actions(request, CreateProfileForm, 'index', Profile(), 'web/profile_create.html')
#
#
# def edit_profile(request):
#     return profile_actions(request, EditProfileForm, 'profile', get_profile(), 'web/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_actions(request, DeleteProfileForm, 'index', get_profile(), 'web/profile_delete.html')
#
#
# class UserRegisterView(RedirectToDashboard):
#     pass
