from django import forms
from catalog.models import Author


class AuthorAddForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control py-4'}))
    date_of_death = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control py-4'}))

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    def save(self, commit=True):
        author = super(AuthorAddForm, self).save(commit=True)
        return author


class AuthorDetailForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control py-4'}))
    date_of_death = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
