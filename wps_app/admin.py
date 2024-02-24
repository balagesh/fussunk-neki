from django.contrib import admin
from .models import Match, Person, Actor, Movie

admin.site.register(Match)
admin.site.register(Person)

admin.site.register(Actor)
admin.site.register(Movie)
