from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import  MessageForm

# ******************** CHATTING ******************************
@login_required
def send_message(request, username):
    #recipient = get_object_or_404(User, username=username)
    if request.method == 'POST':
        #form = MessageForm(request.POST)
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']

        receiver = get_object_or_404(User, id=recipient)
        message = Message(receiver=receiver, subject=subject, body=body, sender=request.user)
        message.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('sentbox')
    else:
        form = MessageForm()
    context = {'form': form, 'users': User.objects.all}
    return render(request, 'send_message.html', context)

@login_required
def inbox(request):
    cnt = Message.objects.filter(receiver=request.user).count()
    messages = Message.objects.filter(receiver=request.user)
    context = {'messages': messages, 'cnt': cnt}
    return render(request, 'inbox.html', context)

@login_required
def sentbox(request):
    messages = Message.objects.filter(sender=request.user)
    context = {'messages': messages}
    return render(request, 'sentbox.html', context)