from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from newspaper.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from typing import Any

from django.db.models.query import Q
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.template import loader

from newspaper.models import Redactor, Topic, Newspaper


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Account created successfully.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url='/login/')
def index(request: HttpRequest) -> HttpResponse:

    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspaper = Newspaper.objects.count()

    list_topics = Topic.objects.all()
    list_redactors = Redactor.objects.all()
    list_newspaper = Newspaper.objects.all()

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspaper": num_newspaper,
        "list_topics": list_topics,
        "list_redactors": list_redactors,
        "list_newspaper": list_newspaper,
    }

    return render(request, "home/index.html", context=context)
