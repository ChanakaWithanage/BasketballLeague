from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from accounts.forms import SignUpForm
from accounts.models import User
from sitestats.models import Stat


def signup_view(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            stat = Stat()
            stat.user = user
            stat.login_time = user.last_login
            stat.save()
            return redirect('fixtures:scoreboard')
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': signup_form})


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            stat = Stat()
            stat.user = user
            stat.login_time = user.last_login
            stat.save()
            return redirect('fixtures:scoreboard')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': login_form})


def logout_view(request):
    if request.method == 'POST':
        try:
            temp_user = User.objects.get(id=request.user.id)
            stats = Stat.objects.filter(user=temp_user)
            logout(request)
            for stat in stats:
                stat.logout_time = timezone.now()
                stat.save()
            return redirect('accounts:login')
        except ObjectDoesNotExist:
            return HttpResponse("Exception: User data not found")

