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

def competition_details(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)
    return render(request, 'cars_competition/competition_details.html', {'competition': competition})

@login_required
def add_to_basket(request, id):
    competition = get_object_or_404(Competition, id=id)
    if request.method == 'POST':
        ticket_count = int(request.POST['ticket_count'])
        if ticket_count > 0 and ticket_count <= (competition.total_tickets - competition.tickets_sold):
            basket_item, created = BasketItem.objects.get_or_create(
                user=request.user,
                competition=competition,
                defaults={'ticket_count': ticket_count}
            )
            if not created:
                basket_item.ticket_count += ticket_count
                basket_item.save()
            return redirect('view_basket')
    return redirect('competition_detail', id=competition.id)

@login_required
def view_basket(request):
    basket_items = BasketItem.objects.filter(user=request.user)
    total_cost = sum(item.competition.ticket_price * item.ticket_count for item in basket_items)
    return render(request, 'cars_competition/view_basket.html', {'basket_items': basket_items, 'total_cost': total_cost})