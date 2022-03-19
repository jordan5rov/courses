from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.forms import Textarea

from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormMixin
from petstagram.web.models import PetPhoto


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH
    )
    picture = forms.URLField()
    date_of_birth = forms.DateTimeField()
    description = forms.CharField(
        widget=Textarea,
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(
        choices=Profile.GENDERS
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user
        )
        if commit:
            profile.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
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
