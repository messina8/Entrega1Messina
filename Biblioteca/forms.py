import datetime

from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    surname = forms.CharField(label='surname', max_length=30)
    id_number = forms.IntegerField(label='id_number')
    address = forms.CharField(label='address', max_length=30)


class BookForm(forms.Form):
    isbn = forms.CharField(label='isbn', max_length=15)
    title = forms.CharField(label='title', max_length=60)
    author = forms.CharField(label='author', max_length=60)
    theme = forms.CharField(label='theme', max_length=20)


class InvoiceForm(forms.Form):
    client_name = forms.CharField(label='client_name', max_length=40)
    book_id = forms.IntegerField(label='book_id')
    total = forms.IntegerField(label='total')


class OwnedBookForm(forms.Form):
    isbn = forms.CharField(label='isbn', max_length=15)
    title = forms.CharField(label='title', max_length=60)
    author = forms.CharField(label='author', max_length=60)
    theme = forms.CharField(label='theme', max_length=20)
    read = forms.BooleanField(label='read', widget=forms.CheckboxInput, required=False)
    read_date = forms.DateField(label='read_date', required=False,
                                widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))


class NewJournalEntryForm(forms.Form):
    date = forms.DateField(label='entry_date', required=False, initial=datetime.datetime.today().strftime('%Y-%m-%d'),
                           widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    text = forms.CharField(widget=forms.Textarea)


