from django import forms


class SearchForm(forms.Form):
    trainer_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by trainer name',
            }
        )
    )

