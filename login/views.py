from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required

from login.forms import ProfileUpdate


def login(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            passwrd = form.cleaned_data.get('password')

            user = authenticate(username=username, password=passwrd)

            if user is not None:
                auth_login(request, user)

                if next_url:
                    return redirect(next_url)
                return render(request, 'home.html', {'welcome_message': f'Welcome back, {user}!'})

            else:
                form = AuthenticationForm()
                return render(request, "login/login.html", {'form': form,
                                                            'message': 'Incorrect credentials, please try again.'})

        else:
            form = AuthenticationForm()
            return render(request, "login/login.html", {'form': form,
                                                        'message': 'Incorrect credentials, please try again.'})

    form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home.html', {'welcome_message': f'Welcome {username}, enjoy your stay!'})

        else:
            form = UserCreationForm()
            return render(request, 'login/login.html', {'form': form, 'message': 'Incorrect data, please try again.'})
    else:
        form = UserCreationForm()

    return render(request, 'login/login.html', {'form': form})


@login_required
def profile(request):
    user_data = {}
    if request.user.is_authenticated:

        user_data = {'username': request.user.username,
                     'email': request.user.email,
                     'full_name': request.user.first_name + ' ' + request.user.last_name,
                     'picture': ''  # should get avatar
                     }
    return render(request, 'login/profile.html', user_data)


def edit_profile(request):
    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        form = ProfileUpdate(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.email = data['mail']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            return redirect(profile)

        else:
            form = ProfileUpdate()
            return render(request, 'login/login.html', {'form': form, 'message': 'Incorrect data, please try again.'})
    else:
        form = ProfileUpdate()

    return render(request, 'login/login.html', {'form': form})
