from django.contrib import admin
from image_cropping import ImageCroppingMixin
from startupweekenddo.models import (
    Event, Facilitator, Mentor, Sponsor, Judge, Organizer,
    Collaborator, Schedule, ScheduleItem, Question
)
from mezzanine.pages.admin import PageAdmin


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


class EventAdmin(ImageCroppingMixin, PageAdmin):
    inlines = [SponsorInline, OrganizerInline, CollaboratorInline, JudgeInline, MentorInline, FacilitatorInline]
    list_display = ['title', 'start_date', 'status']


class ScheduleItemInline(admin.TabularInline):
    model = ScheduleItem
    ordering = ['time']
    extra = 0


class ScheduleAdmin(admin.ModelAdmin):
    inlines = [ScheduleItemInline]
    list_display = ['id', 'event']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'rendered_answer', 'order']
    list_editable = ['order']

    def rendered_answer(self, obj):
        return obj.answer

    rendered_answer.allow_tags = True
    rendered_answer.short_description = 'Answer'

admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Question, QuestionAdmin)
