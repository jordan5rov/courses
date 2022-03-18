from django.views import generic as views
from django.shortcuts import redirect

from petstagram.web.models import PetPhoto


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
