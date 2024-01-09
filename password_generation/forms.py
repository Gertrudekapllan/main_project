from django import forms


class UserInputForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

