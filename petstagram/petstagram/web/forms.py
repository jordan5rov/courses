from django import forms

from petstagram.web.helpers import BootstrapFormMixin
from petstagram.web.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
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
