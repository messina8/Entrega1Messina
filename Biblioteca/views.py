from django.http import HttpResponse
from django.shortcuts import render
from Biblioteca.models import Book, Invoices, Clients
from Biblioteca.forms import ClientForm, InvoiceForm, BookForm


def home(request):
    context = {'welcome_message': 'Welcome to El Rio bookshop management system.'}
    return render(request, 'home.html', context)


def books(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'biblioteca/books.html', {'form': form, 'message': 'Enter book information'})
    else:
        form = BookForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            isbn = data.get('isbn')
            title = data.get('title')
            author = data.get('author')
            theme = data.get('theme')

            new_book = Book(isbn=isbn, title=title, author=author, theme=theme)
            new_book.save()
            return render(request, 'biblioteca/books.html', {'message': 'Book created Successfully'})
        else:
            return HttpResponse('biblioteca/books.html', {'form': form, 'message': 'Enter book information'})


def clients(request):
    if request.method == 'GET':
        form = ClientForm()
        return render(request, 'biblioteca/clients.html', {'form': form, 'message': 'Enter client information'})
    else:
        form = ClientForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            name = data.get('name')
            surname = data.get('surname')
            id_number = data.get('id_number')
            address = data.get('address')

            new_client = Clients(name=name, surname=surname, id_number=id_number, address=address)
            new_client.save()
            return render(request, 'biblioteca/clients.html', {'message': 'New client successfully generated'})
        else:
            return HttpResponse('biblioteca/clients.html')


def invoice(request):
    if request.method == 'GET':
        form = InvoiceForm()
        return render(request, 'biblioteca/invoice.html', {'form': form, 'message': 'Enter invoice details'})
    else:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            client_name = data.get('client_name')
            book_id = data.get('book_id')
            total = data.get('total')

            new_invoice = Invoices(client_name=client_name,
                                   book_id=book_id, total=total)
            new_invoice.save()
            return render(request, 'biblioteca/invoice.html', {'message': 'Invoice created successfully'})
        else:
            return HttpResponse('biblioteca/invoice.html', {'message': 'error'})


def client_search(request):
    return render(request, 'biblioteca/clientsearch.html')


def search(request):
    if request.GET['client_name']:
        client_name = request.GET['client_name']
        client = Clients.objects.filter(name__icontains=client_name)
        return render(request, "biblioteca/searchresult.html", {'clients': client,
                                                                'message': f'searching for {client_name}'})
    else:
        message = "No data to search"
    return render(request, 'biblioteca/clientsearch.html', {'message': message})


def owned_books(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})


def to_do(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})


def timetable(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})


def user_chat(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})


def journal(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})

