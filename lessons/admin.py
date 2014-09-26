from django.contrib import admin
from lessons.models import Practice, Lesson, Instructor

class TeachingsInline(admin.TabularInline):
    model = Practice.teachings.through
    extra = 1

class LessonAdmin(admin.ModelAdmin):
    inlines = [
        TeachingsInline,
    ]
    list_display = ('title', 'level', 'style')
    list_filter = ('level', 'style', 'title')

admin.site.register(Lesson, LessonAdmin)

class PracticeAdmin(admin.ModelAdmin):
    inlines = [
        TeachingsInline,
    ]
    exclude = ('lessons',)
    list_display = ('date','overview', 'location')
    list_filter = ['date', 'overview', 'location']

admin.site.register(Practice, PracticeAdmin)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_lead', 'is_follow','is_active')
    list_filter = ('is_lead', 'is_follow', 'year', 'is_active')

admin.site.register(Instructor, InstructorAdmin)
