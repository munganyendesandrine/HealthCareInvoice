from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .forms import HealthPostForm,PatientForm,HealthPostForm2
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import HealthPost,Patient,WelcomeMsgRecipients
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
   
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login/')
def hcpost_info(request):
    current_user = request.user
    if request.method == 'POST':
        form = HealthPostForm(request.POST, request.FILES)
        if form.is_valid():
            hcpost = form.save(commit=False)
            hcpost.user = current_user
            hcpost.save()
        return redirect('welcome')

    else:
       form = HealthPostForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def patient_info(request):
    current_user = request.user
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = current_user
            patient.save()
        return redirect('welcome')

    else:
       form = PatientForm()
    return render(request, 'patient.html', {"form": form})

@login_required(login_url='/accounts/login/')
def service_details(request):
    current_user = request.user
    if request.method == 'POST':
        form = HealthPostForm(request.POST, request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = current_user
            details.save()
        return redirect('welcome')

    else:
       form = HealthPostForm()
    return render(request, 'patient.html', {"form": form})
    
def send_mail(request):
    if request.method == 'POST':
        form = HealthPostForm2(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = WelcomeMsgRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('send_mail')
            #.................
    return render(request, 'registration/hcform1.html')

