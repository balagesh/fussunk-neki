from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Match, Person, Actor, Movie
from .forms import MatchForm, RegisterForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def app_homepage(request):
    matches = Match.objects.all()
    person = Person.objects.all()
    return render(request, 'homepage.html', {'matches': matches, 'person': person})

def matchform(request):
    return render(request, 'matchform.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            newname = form.cleaned_data
            regact = Actor(name = newname['name'])
            regact.save()
            messages.success(request, "Field created successfully")
            return redirect("app_homepage")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)

def newmatch(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            newname = form.cleaned_data
            regmatch = Match(name = newname['name'])
            regmatch.save()
            messages.success(request, "Match field created successfully")
            return redirect("app_homepage")
    else:
        form = MatchForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)

def newplayer(request):
    return render(request, 'newplayer.html')