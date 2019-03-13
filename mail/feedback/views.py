from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

def index(request):
    return render(request, 'mailbox.html')


def mailbox(request):
    subject = 'Sender mail: %r' % request.GET['subject']

    send_mail(subject,
              request.GET['body'],
              'amitrcc2441@gmail.com',
              ['yitujufej@next-mail.info'],
              fail_silently=False)
    return render(request,'index.html')






