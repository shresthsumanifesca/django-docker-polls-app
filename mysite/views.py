from django.contrib.auth.views import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/polls')
    else:
        return login(request)

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')

    else:
        f = UserCreationForm()

    return render(request, 'accounts/signup', {'form': f})
