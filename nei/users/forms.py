from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
