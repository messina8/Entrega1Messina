from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout, authenticate


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            passwrd = form.cleaned_data.get('password')

            user = authenticate(username=username, password=passwrd)

            if user is not None:
                auth_login(request, user)

                return render(request, 'home.html', {'welcome_message': f'Welcome back, {user}!'})

            else:
                return render(request, "home.html", {'welcome_message': 'Incorrect credentials'})

        else:
            return render(request, 'home.html', {'welcome_message': 'Incorrect form'})

    form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home.html', {'welcome_message': f'Welcome {username}, enjoy your stay!'})


def profile(request):
    pass
