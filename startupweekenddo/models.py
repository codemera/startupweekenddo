from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from django.utils.translation import ugettext as _


class Event(models.Model):
    start_date = models.DateField(verbose_name=_('Start Date'), blank=False, null=False)
    end_date = models.DateField(verbose_name=_('End Date'), blank=True, null=True)
    title = models.CharField(max_length=50, unique=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='event/', verbose_name=_('Main Image'), null=True, blank=True)
    registration_uri = models.URLField(verbose_name=_('Registration Link'))

    banner = ImageCropField(upload_to='event/banner/', verbose_name='Banner', blank=True, null=True)
    logo = ImageCropField(upload_to='event/logo/', verbose_name='Logo', blank=True, null=True)

    banner_crop = ImageRatioField('banner', '800x400')  # TODO: Define these sizes
    logo_crop = ImageRatioField('logo', '400x400')  # TODO: Define these sizes

    def __str__(self):
        return self.title

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
    event = models.ForeignKey('Event', null=False)
    url = models.URLField()

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
    twitter = models.CharField(max_length=25)

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
    schedule = models.ForeignKey('Schedule')
    time = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "{event} [{time}] {desc}".format(event=self.schedule.event.title,
                                                time=self.time, desc=self.description)