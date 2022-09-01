from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required

from login.forms import ProfileUpdate
from login.models import Profile, LogHistory


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
                log = LogHistory(user_id=request.user.id, log_in=True)
                log.save()

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
        pictures = Profile.objects.filter(user=request.user.id)
        user_data = {'username': request.user.username,
                     'email': request.user.email,
                     'full_name': request.user.first_name + ' ' + request.user.last_name,
                     'picture': pictures[0].avatar.url,
                     'join_date': request.user.date_joined
                     }
    return render(request, 'login/profile.html', user_data)


def edit_profile(request):
    user = User.objects.get(username=request.user.username)
    avatar_db = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            user.email = data['mail']  # if data['mail'] is not None else request.user.email
            user.first_name = data['first_name']  # if data['first_name'] is not None else request.user.first_name
            user.last_name = data['last_name']  # if data['last_name'] is not None else request.user.last_name
            if avatar_db is not None:
                avatar_db.avatar=data['avatar']
            else:
                avatar_db = Profile(user=user, avatar=data['avatar'])
            user.save()
            avatar_db.save()

            return redirect(profile)

        else:
            form = ProfileUpdate()
            return render(request, 'login/profile_update.html', {'form': form,
                                                                 'message': 'Incorrect data, please try again.'})
    else:
        form = ProfileUpdate()

    return render(request, 'login/profile_update.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'welcome_message': f'Password changed correctly.'})

        else:
            form = PasswordChangeForm(request.user)
            return render(request, 'login/login.html', {'form': form, 'message': 'Incorrect data, please try again.'})
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'login/login.html', {'form': form})
