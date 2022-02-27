from django.urls import path

from exam_music_app_problem.web.views import show_index, create_album, details_album, edit_album, delete_album, \
    delete_profile, show_profile, create_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>/', details_album, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/details/', show_profile, name='details profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/create/', create_profile, name='create profile')
)
