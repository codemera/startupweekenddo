from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    place = models.CharField(max_length=100)

    def __str__(self):
        return 'dia ' + self.date + ', lugar ' + self.place

class SponsorCategory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sponsors/')
    categori = models.ForeignKey(SponsorCategory)
    url = models.URLField(null=True)

    def __srt__(self):
        return self.name + ' categoria '+ self.categori


class Person(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='person/')

    def __str__(self):
        return self.name


class Facilitator(Person):
    bio = models.TextField(max_length=500)
    twitter = models.TextField(max_length=25)

    def __str__(self):
        return self.name


class Mentor(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Judges(Mentor):

    def __srt__(self):
        return self.name


class Organizer(Person):

    def __srt__(self):
        return self.name


class Collaborator(Person):

    def __str__(self):
        return self.name
