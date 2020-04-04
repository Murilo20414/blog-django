from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return HttpResponse('')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = RegistrationForm()
        args = {'form' : form}
        return render(request, 'users/create_user.html', args)


