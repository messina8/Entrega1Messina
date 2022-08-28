from django import forms


class ProfileUpdate(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    mail = forms.EmailField()
