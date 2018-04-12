from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/polls')
    else:
        return login(request)

def custom_logout(request):
    return HttpResponseRedirect('/irrelevant')
    # if request.user.is_authenticated:

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')

    else:
        f = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': f})
