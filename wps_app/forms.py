from django.forms import ModelForm, models
from django import forms
from .models import Match, Person, Actor, Movie

from formset.widgets import Selectize, SelectizeMultiple

class RegisterForm(forms.Form):
    name = forms.CharField(label="Actor's name", max_length=100)
    #distance_unit = forms.ChoiceField(choices=MEASUREMENT_UNITS, label='Distance in', widget=forms.RadioSelect(choices=MEASUREMENT_UNITS), initial='KM'  )

class MatchForm(forms.Form):
    team1 = forms.CharField(max_length=50)
    team2 = forms.CharField(max_length=50)
    goals1 = forms.IntegerField()
    goals2 = forms.IntegerField()
    date = forms.DateField()
    person = forms.ModelMultipleChoiceField(
        queryset=Person.objects.all(),
        widget=SelectizeMultiple(attrs={'size':'10'}, search_lookup='name__icontains'),

        #widget=forms.CheckboxSelectMultiple
    )
    #person = forms.ManyToManyField(to=Person, related_name="matches")