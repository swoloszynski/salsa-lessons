from django.contrib import admin
from lessons.models import Practice, Lesson

class PracticeAdmin(admin.ModelAdmin):
    fields = ['date', 'location', 'overview', 'lessons', 'notes']

admin.site.register(Practice, PracticeAdmin)
admin.site.register(Lesson)

