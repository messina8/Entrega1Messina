import datetime

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Biblioteca.models import Book, Invoices, Clients, OwnedBooks, JournalEntry, ToDoItem
from Biblioteca.forms import *


def home(request):
    context = {'welcome_message': 'Welcome to El Rio Time management system.'}
    if request.user.is_authenticated:
        context = {'welcome_message': f'Welcome to El Rio Time management system, {request.user.username}.'}
    return render(request, 'home.html', context)


def about(request):
    context = {'welcome_message': 'Welcome to El Rio Time management system.'}
    return render(request, 'about.html', context)


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


@login_required
def owned_books(request):
    book_list = OwnedBooks.objects.filter(user=request.user)
    return render(request, 'biblioteca/owned_books.html', {'books': book_list})


@login_required()
def new_owned_book(request):
    if request.method == 'POST':
        new_book_form = OwnedBookForm(request.POST)

        if new_book_form.is_valid():
            info = new_book_form.cleaned_data
            new = OwnedBooks(isbn=info['isbn'], title=info['title'], author=info['author'], theme=info['theme'],
                             read=info['read'], read_date=info['read_date'], user=request.user)
            new.save()
            return redirect(owned_books)

        else:
            form = OwnedBookForm()
            return render(request, 'login/login.html', {'form': form, 'message': 'Incorrect data, please try again.'})
    else:
        form = OwnedBookForm()

    return render(request, 'biblioteca/new_owned_book.html', {'form': OwnedBookForm})


@login_required()
def set_book_read(request, book_id):
    book = OwnedBooks.objects.get(id=book_id)
    book.read = True
    book.read_date = datetime.datetime.today().strftime('%Y-%m-%d')
    book.save()
    return render(request, 'biblioteca/clean_base.html', {'message': f'The book {book.title} by {book.author}'
                                                                     f' was successfully set as read.',
                                                          'url': '/management/owned_books/'})


@login_required
def journal(request):
    entry_list = JournalEntry.objects.filter(user=request.user)
    entry_list.order_by('-date')
    return render(request, 'biblioteca/journal.html', {'entry_list': entry_list})


@login_required()
def new_journal_entry(request):
    if request.method == 'POST':
        form = NewJournalEntryForm(request.POST)

        if form.is_valid():
            entry = form.cleaned_data
            new = JournalEntry(date=entry['date'], entry=entry['text'], user=request.user)

            try:
                new.save()
            except IntegrityError:
                return render(request,
                              'biblioteca/clean_base.html',
                              {'form': form,
                               'message': 'That date already exists, try editing.',
                               'hide': False,
                               'url': '../journal'})

            return redirect(journal)
        else:
            render(request, 'biblioteca/clean_base.html', {'form': form,
                                                           'message': 'Date format incorrect./nPlease use yyyy-mm-dd',
                                                           'hide': True})
    return render(request, 'biblioteca/clean_base.html', {'form': NewJournalEntryForm, 'hide': True})


@login_required()
def edit_entry(request, entry_id):  # should make a big "if:" to check if the entry belongs to the user.
    entry = JournalEntry.objects.get(id=entry_id)
    if request.method == 'POST':
        form = NewJournalEntryForm(request.POST, )

        if form.is_valid():
            entry.entry = form.cleaned_data['text']
            entry.save()
            return redirect('Journal')
    else:
        form = NewJournalEntryForm(initial={'date': entry.date, 'text': entry.entry})
    return render(request, 'biblioteca/edit_entry.html', {'entry': entry, 'form': form})


@login_required()
def read_entry(request, entry_id):
    text = JournalEntry.objects.filter(id=entry_id)
    return render(request, 'biblioteca/read_entry.html', {'entry': text[0]})


@login_required
def to_do(request):
    to_do_list = ToDoItem.objects.filter(user=request.user, done=False)
    to_do_list.order_by('-expiration_date')
    return render(request, 'biblioteca/to_do.html', {'to_do_list': to_do_list})


@login_required
def done(request):
    to_do_list = ToDoItem.objects.filter(user=request.user, done=True)
    to_do_list.order_by('-expiration_date')
    return render(request, 'biblioteca/to_do.html', {'to_do_list': to_do_list, 'done': True})


def new_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data
            new = ToDoItem(expiration_date=task['due'], task=task['task'],
                           task_description=task['description'], user=request.user)

            new.save()

            return redirect(to_do)
        else:
            render(request, 'biblioteca/clean_base.html', {'form': form,
                                                           'message': 'Date format incorrect./nPlease use yyyy-mm-dd',
                                                           'hide': True})
    return render(request, 'biblioteca/clean_base.html', {'form': NewTaskForm, 'hide': True})


@login_required()
def set_task_done(request, task_id):
    item = ToDoItem.objects.get(id=task_id)
    item.done = True
    item.time_when_done = datetime.datetime.now()
    item.save()
    return render(request, 'biblioteca/clean_base.html',
                  {'message': f'The task {item.task} was successfully set as read.', 'url': '/management/to_do/'})


@login_required
def timetable(request):
    return render(request, 'home.html', {'welcome_message': f'Not yet, buddy. Give me some time.'})


