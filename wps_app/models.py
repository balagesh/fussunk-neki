from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Movie(models.Model):
    name = models.CharField(max_length=50)
    cast = models.ManyToManyField(to=Actor, blank=True, null=True, related_name="movies")

class Person(models.Model):
    name = models.CharField(max_length=50)
    #match = models.ForeignKey(Match, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Match(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    goals1 = models.PositiveIntegerField(default=0)
    goals2 = models.IntegerField(default=0)
    date = models.DateField(null=True)
    person = models.ManyToManyField(to=Person, related_name="matches")

    def __str__(self):
        return f"{self.team1} - {self.team2}: {self.goals1} - {self.goals2} {self.date}"

