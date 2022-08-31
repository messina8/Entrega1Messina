from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from chat.forms import SendMessageForm
from chat.models import Message
from login.models import Profile


# Create your views here.


@login_required
def messages(request):
    received_messages = Message.objects.filter(target=request.user.id)
    for i in received_messages:

        pass
    data = {'received_messages': received_messages}

    return render(request, 'chat/messages.html', data)


def user_list(request):
    users = User.objects.all()
    return render(request, 'chat/users.html', {'users': users})


def send_message(request, user_id):
    to = User.objects.filter(id=user_id)
    target = to[0]
    context = {}
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        context = {'form': form, 'target_name': target.username}
        if form.is_valid():
            message = form.cleaned_data['message']
            msg = Message(sender=request.user, message=message, target=to[0])
            msg.save()
            return redirect(messages)  # render(request, 'chat/send_message.html', context)
        else:
            form = SendMessageForm()
            return render(request, 'chat/send_message.html', form)
    else:
        form = SendMessageForm()
        context = {'form': form, 'target_name': target.username}
        return render(request, 'chat/send_message.html', context)

    context = {'form': SendMessageForm(), 'target_name': target.username}
    return render(request, 'chat/send_message.html', context)


def read_message(request):
    pass


def reviews(request):  # will get done if I have enough time
    pass


def new_review(request):  # will get done if I have enough time
    pass
