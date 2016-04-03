from django.db import models

# Create your models here.

class Event(models.Model):
    first_date = models.DateField(verbose_name='Primer Dia', blank=True, null=True)
    second_date = models.DateField(verbose_name='Segundo Dia', blank=True, null=True)
    third_date = models.DateField(verbose_name='Tercer Dia', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='event/', verbose_name='Imagen principal')
    registration = models.URLField(verbose_name='Link de registro')
    banner = models.ImageField(upload_to='event/banner/', verbose_name='Banner', blank=True, null=True)
    logo = models.ImageField(upload_to='event/logo/', verbose_name='Logo', blank=True, null=True)

    def __str__(self):
        return self.title


class SponsorCategory(models.Model):
    number_order = models.IntegerField(verbose_name='Posicion')
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sponsors/')
    categori = models.ForeignKey(SponsorCategory)
    url = models.URLField()

    def __str__(self):
        return self.name + ' categoria ' + self.categori.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='person/')
    visible = models.BooleanField()

    def __str__(self):
        return self.name


class Facilitator(Person):
    bio = models.TextField(max_length=500)
    twitter = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Mentor(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Judges(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500)

    def __srt__(self):
        return self.name


class Organizer(Person):
    number_order = models.IntegerField(unique=True, verbose_name='Numero de orden')

    def __srt__(self):
        return self.name


class Collaborator(Person):
    pass

    def __str__(self):
        return self.name
