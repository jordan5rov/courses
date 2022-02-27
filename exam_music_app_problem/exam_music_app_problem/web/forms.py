from django import forms

from exam_music_app_problem.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name:',
            'artist': 'Artist:',
            'genre': 'Genre:',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price:',
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name:',
            'artist': 'Artist:',
            'genre': 'Genre:',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price:',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name:',
            'artist': 'Artist:',
            'genre': 'Genre:',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price:',
        }
