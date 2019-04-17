from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .forms import HealthPostForm
from django.http import HttpResponse, Http404,HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
   
    return render(request,'welcome.html')

def send_mail(request):
    if request.method == 'POST':
        form = HealthPostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = WelcomeMsgRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('send_mail')
            #.................
    return render(request, 'registration/hcform1.html')
