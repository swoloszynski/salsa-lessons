from django.contrib import admin
from lessons.models import Practice, Lesson

class PracticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['overview', 'lessons', 'notes']}),
        ('Date and Location', {'fields': ['date', 'location'], 'classes': ['collapse']}),
    ]

admin.site.register(Practice, PracticeAdmin)
admin.site.register(Lesson)
