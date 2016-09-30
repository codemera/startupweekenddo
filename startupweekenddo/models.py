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
    location = models.CharField(_('Location'), max_length=100, blank=True, null=True)
    city = models.CharField(_('City'), max_length=100, blank=False, null=False)
    registration_uri = models.URLField(verbose_name=_('Registration Link'))

    banner = ImageCropField(upload_to='event/banner/', verbose_name='Banner', blank=True, null=True)
    logo = ImageCropField(upload_to='event/logo/', verbose_name='Logo', blank=True, null=True)

    banner_crop = ImageRatioField('banner', '2000x1200')

    logo_crop = ImageRatioField('logo', '400x400')

    youtube_video_id = models.CharField(max_length=50, blank=True, null=True)

    participants = models.PositiveIntegerField(_('Participants'), default=0)

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
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

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
    name = models.CharField(_('Name'), max_length=50)
    image = ImageCropField(_('Picture'), upload_to='sponsors/')
    category = models.IntegerField(_('Category'), choices=SPONSOR_CATEGORIES, null=False, blank=False)
    event = models.ForeignKey('Event', null=False, related_name="sponsors")
    url = models.URLField(blank=True, null=True)

    image_crop = ImageRatioField('image', '500x400')  # TODO: Define these sizes

    def __str__(self):
        return "[{category}] {name}".format(category=self.category, name=self.name)

    class Meta:
        ordering = ['event', 'category', 'name']
        unique_together = [('event', 'name')]
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')


class Person(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    image = ImageCropField(_('Picture'), upload_to='person/')
    visible = models.BooleanField(_('Visible'), default=True)
    event = models.ForeignKey('Event', null=False)

    image_crop = ImageRatioField('image', '300x300')  # TODO: Define these sizes

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['event', 'name']
        verbose_name = _('Person')
        verbose_name_plural = _('People')


class Facilitator(Person):
    bio = models.TextField(max_length=500)
    twitter = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Facilitator')
        verbose_name_plural = _('Facilitators')


class Mentor(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Mentor')
        verbose_name_plural = _('Mentors')


class Judge(Person):
    bio = models.TextField(max_length=500)
    position = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Judge')
        verbose_name_plural = _('Judges')


class Organizer(Person):
    order = models.PositiveIntegerField(verbose_name=_('Order'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['event', 'order']
        verbose_name = _('Organizer')
        verbose_name_plural = _('Organizers')


class Collaborator(Person):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Collaborator')
        verbose_name_plural = _('Collaborators')


class Schedule(models.Model):
    event = models.OneToOneField('Event')

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')


class ScheduleItem(models.Model):
    schedule = models.ForeignKey('Schedule', related_name='items')
    time = models.DateTimeField(_('Time'), null=False, blank=False)
    title = models.CharField(_('Title'), max_length=100)
    description = models.CharField(_('Description'), max_length=500, blank=True, null=True)

    def __str__(self):
        return "{event} [{time}] {desc}".format(event=self.schedule.event.title,
                                                time=self.time, desc=self.description)

    class Meta:
        verbose_name = _('Schedule Item')
        verbose_name_plural = _('Schedule Items')


class QuestionCategory(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=200)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'id']
        verbose_name = _('Question Category')
        verbose_name_plural = _('Question Categories')


class Question(models.Model):
    category = models.ForeignKey('QuestionCategory', related_name='questions', null=True, blank=True)
    question = models.CharField(_('Question'), unique=True, max_length=200)
    answer = RichTextField(_('Answer'), blank=False, null=False)

    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return "{q}: {a}".format(q=self.question, a=self.answer)

    class Meta:
        ordering = ['category__order', 'order', 'id']
        verbose_name = _('Frequent Question')
        verbose_name_plural = _('Frequent Questions')


class HomePageData(models.Model):
    header = RichTextField(_('Header'), blank=False, null=False)
    about = RichTextField(_('About'), blank=False, null=False)
    embed_link_id = models.CharField(max_length=50, null=True, blank=True)
    video_description = RichTextField(_('Video Description'), blank=False, null=False)

    enabled = models.BooleanField(_('Enabled'), default=True)
    date_added = models.DateTimeField(_('Date Added'), auto_now_add=True)

    class Meta:
        ordering = ['-date_added', 'enabled']
        verbose_name = _('HomePage Information')
        verbose_name_plural = _('Homepage Information')


class PressRelease(models.Model):
    title = models.CharField(_('Title'), max_length=100, unique=True)
    press_file = models.FileField(_('Press File'), upload_to='press_releases/')
    date_added = models.DateTimeField(_('Date Added'), auto_now_add=True)
    published = models.BooleanField(_('Published?'), default=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Press Release')
        verbose_name_plural = _('Press Releases')
