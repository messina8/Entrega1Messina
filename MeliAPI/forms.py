from django import forms


class PriceCheckForm(forms.Form):
    product_name = forms.CharField(label='Product Name:', max_length=40)
    used_search = forms.BooleanField(label='Search Used', widget=forms.CheckboxInput, required=False)


class CompraForm(forms.Form):
    monto = forms.IntegerField(label='Monto')
    recibo = forms.BooleanField(label='Recibo', widget=forms.CheckboxInput, required=False)


class VentaForm(forms.Form):
    efectivo = forms.IntegerField(label='Efectivo:', required=False)
    tarjeta = forms.IntegerField(label='Tarjeta:')
    mercadopago = forms.BooleanField(label='MP', widget=forms.CheckboxInput, required=False)
