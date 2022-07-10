from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from bs4 import BeautifulSoup
from .models import Client
from .forms import reg_form


def home(request):
    if request.GET.get('tok') is not None and request.GET.get('redir') is not None:
        request.session['tok'] = request.GET.get('tok')
        request.session['redir'] = request.GET.get('redir')
    if request.user.is_authenticated:
        record_obj = get_object_or_404(Client, user=request.user)
        plan = record_obj.plan
        p_time = record_obj.paid_time
        return render(request, 'user_auth/home.html', {'plan': plan, 'p_time': p_time})
    else:
        return render(request, 'user_auth/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'user_auth/signup.html', {'form': UserCreationForm})
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('two_factor:setup')
            except IntegrityError:
                return render(request, 'user_auth/signup.html',
                              {'form': UserCreationForm, 'errormessage': 'The username is taken'})
        else:
            return render(request, 'user_auth/signup.html', {'form': UserCreationForm, 'errormessage': 'The passwords do not match'})

'''
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'user_auth/login.html', {'form': AuthenticationTokenForm})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user_auth/login.html', {'form': AuthenticationTokenForm,
                                                           'errormessage': 'The username and password do not match'})
        else:
            login(request, user)
            return redirect('user_auth:home')
'''


def get_selected(tar_html):
    return BeautifulSoup(str(tar_html), 'html.parser').find('option', selected=True)['value']


def register_user(request):
    if request.method == 'GET':
        return render(request, 'user_auth/createform.html', {'form': reg_form()})
    if request.method == 'POST':
        form_obj = reg_form(request.POST)
        if form_obj.is_valid():
            user_plan = get_selected(form_obj['plan'])
            Client(full_name=form_obj['full_name'], plan=user_plan, user=request.user).save()
            if user_plan == 'paid':
                return redirect('user_auth:p_portal')
            else:
                return redirect('user_auth:home')


def payment_portal(request):
    tok = request.session['tok']
    redir = request.session['redir']
    return render(request, 'user_auth/p_portal.html', {'tok': tok, 'redir': redir})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_auth:home')


@login_required()
def logout_debug(request):
    logout(request)
    return render(request, 'user_auth/debug_logout.html')

