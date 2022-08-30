from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

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
    pass


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
            return render(request, 'chat/send_message.html', context)
        else:
            form = SendMessageForm()
            return render(request, 'chat/send_message.html', context)
    else:
        form = SendMessageForm()
        data = {'form': form, 'target_name': target.username}
        return render(request, 'chat/send_message.html', context)

    data = {'form': SendMessageForm(), 'target_name': target.username}
    return render(request, 'chat/send_message.html', context)


def read_message(request):
    pass


def reviews(request):
    pass


def new_review(request):
    pass
