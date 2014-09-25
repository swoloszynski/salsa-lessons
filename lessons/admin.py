from django.contrib import admin
from lessons.models import Practice, Lesson, Instructor

class TeachingsInline(admin.TabularInline):
    model = Practice.teachings.through
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [
        TeachingsInline,
    ]

class PracticeAdmin(admin.ModelAdmin):
    inlines = [
        TeachingsInline,
    ]
    exclude = ('lessons',)

admin.site.register(Practice, PracticeAdmin)
admin.site.register(Lesson)
admin.site.register(Instructor)
