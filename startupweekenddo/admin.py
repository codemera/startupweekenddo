from django.contrib import admin
from image_cropping import ImageCroppingMixin
from startupweekenddo.models import (
    Event, Facilitator, Mentor, Sponsor, Judge, Organizer,
    Collaborator, Schedule, ScheduleItem
)


class FacilitatorInline(ImageCroppingMixin, admin.TabularInline):
    model = Facilitator
    extra = 0


class OrganizerInline(ImageCroppingMixin, admin.TabularInline):
    model = Organizer
    extra = 0
    ordering = ['order']


class JudgeInline(ImageCroppingMixin, admin.TabularInline):
    model = Judge
    extra = 0


class CollaboratorInline(ImageCroppingMixin, admin.TabularInline):
    model = Collaborator
    extra = 0


class MentorInline(ImageCroppingMixin, admin.TabularInline):
    model = Mentor
    extra = 0


class SponsorInline(ImageCroppingMixin, admin.TabularInline):
    model = Sponsor
    extra = 0


class EventAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [SponsorInline, OrganizerInline, CollaboratorInline, JudgeInline, MentorInline]
    list_display = ['title', 'start_date', 'place']


class ScheduleItemInline(admin.TabularInline):
    model = ScheduleItem
    ordering = ['time']
    extra = 0


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [ScheduleItemInline]
    list_display = ['id', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)
