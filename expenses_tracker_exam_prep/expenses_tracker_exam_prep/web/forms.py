import os

from django import forms

from expenses_tracker_exam_prep.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        if commit:
            Expense.objects.all().delete()
            self.instance.delete()
            os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')

