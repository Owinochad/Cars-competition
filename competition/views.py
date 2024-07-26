from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreatUserForm, LoginForm

from django.contrib.auth.decorators import login_required
from .models import *


# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):

    return render(request, 'cars_competition/index.html')


@login_required(login_url="login-user")
def dashboard(request):
    return render(request, 'cars_competition/dashboard.html')


def login_user(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                 
                 auth.login(request, user)

                 return redirect('dashboard')
    

    context = {
        'loginform': form,
    }

    return render(request, 'cars_competition/login.html', context=context)


def logout_user(request):

    auth.logout(request)

    return redirect("index")


def register_user(request):

    form = CreatUserForm()

    if request.method == 'POST':

        form = CreatUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login-user")

    context = {
        'registerform':form
    }

    return render(request, 'cars_competition/register.html', context=context)

def competitions(request):
    competitions = Competition.objects.all()
    return render(request, 'cars_competition/competitions.html', {'competitions': competitions})

def competition(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    return render(request, 'cars_competition/competition.html', {'competition': competition})