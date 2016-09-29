from collections import OrderedDict
from itertools import groupby

from django.db import models
from django.utils.translation import ugettext as _
from image_cropping import ImageCropField, ImageRatioField
from mezzanine.core.models import RichTextField
from mezzanine.pages.models import Page


class Event(Page):
    start_date = models.DateField(verbose_name=_('Start Date'), blank=False, null=False)
    end_date = models.DateField(verbose_name=_('End Date'), blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    registration_uri = models.URLField(verbose_name=_('Registration Link'))

    banner = ImageCropField(upload_to='event/banner/', verbose_name='Banner', blank=True, null=True)
    logo = ImageCropField(upload_to='event/logo/', verbose_name='Logo', blank=True, null=True)

    banner_crop = ImageRatioField('banner', '2000x1200')

    logo_crop = ImageRatioField('logo', '400x400')  # TODO: Define these sizes

    participants = models.PositiveIntegerField(default=0)

    @property
    def sponsors_by_category(self):
        sponsors = sorted(self.sponsors.all(), key=lambda x: x.category)
        cats = dict(SPONSOR_CATEGORIES)
        result = OrderedDict((cat, []) for cat in cats.values())
        for cat, spons in groupby(sponsors, key=lambda x: x.category):
            result[cats.get(cat)].extend(spons)
        return result

    @property
    def judges(self):
        return Judge.objects.filter(event=self)

    @property
    def facilitators(self):
        return Facilitator.objects.filter(event=self)

    @property
    def mentors(self):
        return Mentor.objects.filter(event=self)

    @property
    def organizers(self):
        return Organizer.objects.filter(event=self)

    @property
    def collaborators(self):
        return Collaborator.objects.filter(event=self)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-start_date", "title"]

SPONSOR_DIAMOND = 1
SPONSOR_PLATINUM = 2
SPONSOR_SILVER = 3
SPONSOR_BRONZE = 4
SPONSOR_MEDIA_PARTNER = 5

SPONSOR_CATEGORIES = (
    (SPONSOR_DIAMOND, _('Diamond')),
    (SPONSOR_PLATINUM, _('Platinum')),
    (SPONSOR_SILVER, _('Silver')),
    (SPONSOR_BRONZE, _('Bronze')),
    (SPONSOR_MEDIA_PARTNER, _('Media Partner')),
)


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    image = ImageCropField(upload_to='sponsors/')
    category = models.IntegerField(choices=SPONSOR_CATEGORIES, null=False, blank=False)
    event = models.ForeignKey('Event', null=False, related_name="sponsors")
    url = models.URLField(blank=True, null=True)

    image_crop = ImageRatioField('image', '500x400')  # TODO: Define these sizes

    def __str__(self):
        return "[{category}] {name}".format(category=self.category, name=self.name)

    class Meta:
        ordering = ['event', 'category', 'name']
        unique_together = [('event', 'name')]


class Person(models.Model):
    name = models.CharField(max_length=50)
    image = ImageCropField(upload_to='person/')
    visible = models.BooleanField(default=True)
    event = models.ForeignKey('Event', null=False)

    image_crop = ImageRatioField('image', '300x300')  # TODO: Define these sizes

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['event', 'name']


class Facilitator(Person):
    bio = models.TextField(max_length=500)
    twitter = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class Mentor(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Judge(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Organizer(Person):
    order = models.PositiveIntegerField(verbose_name=_('Order'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['event', 'order']


class Collaborator(Person):
    def __str__(self):
        return self.name


class Schedule(models.Model):
    event = models.OneToOneField('Event')


class ScheduleItem(models.Model):
    schedule = models.ForeignKey('Schedule', related_name='items')
    time = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "{event} [{time}] {desc}".format(event=self.schedule.event.title,
                                                time=self.time, desc=self.description)


class QuestionCategory(models.Model):
    name = models.CharField(unique=True, max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'id']


class Question(models.Model):
    category = models.ForeignKey('QuestionCategory', related_name='questions', null=True, blank=True)
    question = models.CharField(unique=True, max_length=200)
    answer = RichTextField(blank=False, null=False)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{q}: {a}".format(q=self.question, a=self.answer)

    class Meta:
        ordering = ['order', 'id']


class HomePageData(models.Model):
    header = RichTextField(blank=False, null=False)
    about = RichTextField(blank=False, null=False)
    embed_link_id = models.CharField(max_length=50, null=True, blank=True)
    video_description = RichTextField(blank=False, null=False)

    enabled = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', 'enabled']
