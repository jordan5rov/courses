from django.urls import path

from expenses_tracker_exam_prep.web.views import delete_profile, show_index, create_expense, edit_expense, \
    delete_expense, show_profile, edit_profile, create_profile

urlpatterns = (
    path('', show_index, name='home page'),

    path('create/', create_expense,  name='create expense'),
    path('edit/<int:pk>', edit_expense,  name='edit expense'),
    path('delete/<int:pk>', delete_expense,  name='delete expense'),

    path('profile/', show_profile,  name='profile'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/edit', edit_profile,  name='edit profile'),
    path('profile/delete', delete_profile,  name='delete profile'),
)
