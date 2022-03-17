from datetime import date
from random import choices

import instance as instance
from django import forms
from django.core.exceptions import ValidationError

from petstagram.web.helpers import BootstrapFormMixin, DisableFieldsFormMixin
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
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets)
        pet_photos.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
        # exclude = ('first_name', 'last_name', 'picture', 'email', 'description', 'date_of_birth', 'gender')


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        pet = super().save(commit=False)

        pet.user = self.user
        if commit:
            pet.save()

        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or \
                self.MAX_DATE_OF_BIRTH > date_of_birth:
            raise ValidationError(
                'Date of birth must be between 1920/1/1 and now'
            )
        return date_of_birth

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(BootstrapFormMixin, DisableFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ()
