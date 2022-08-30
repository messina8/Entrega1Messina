from django import forms


class SendMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
