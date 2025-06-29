from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search users or posts…',
            'class': 'form-control me-2',
        })
    )
