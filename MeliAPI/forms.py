
from django import forms


class PriceCheckForm(forms.Form):
    product_name = forms.CharField(label='Product Name:', max_length=40)
    used_search = forms.BooleanField(label='Search Used', widget=forms.CheckboxInput, required=False)
