from django.views import generic as views
from django.shortcuts import redirect

from petstagram.web.models import PetPhoto


# def show_home(request):
#     context = {
#         'hide_additional_nav_items': True,
#     }
#     return render(request, 'web/home_page.html', context)
class HomeView(views.TemplateView):
    template_name = 'web/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'web/dashboard.html'
    context_object_name = 'pet_photos'


# def show_dashboard(request):
#     profile = get_profile()
#
#     pet_photos = PetPhoto.objects \
#         .prefetch_related('tagged_pets') \
#         .filter(tagged_pets__user_profile=profile) \
#         .distinct()
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'web/dashboard.html', context)
