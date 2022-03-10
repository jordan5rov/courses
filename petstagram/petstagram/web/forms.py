from random import choices

import instance as instance
from django import forms

from petstagram.web.helpers import BootstrapFormMixin
from petstagram.web.models import Profile, Pet, PetPhoto


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
            }),
            'picture': forms.TextInput(attrs={
                'placeholder': 'Enter your image url',
            }),

        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
            }),
            'picture': forms.TextInput(attrs={
                'placeholder': 'Enter your image url',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description',
                'row': 3,
            }),
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'Enter Date',
                'min': '1920-01-01',
            })
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self):
        pets = list(self.instance.pet_set.all())
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets)
        pet_photos.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
        # exclude = ('first_name', 'last_name', 'picture', 'email', 'description', 'date_of_birth', 'gender')
