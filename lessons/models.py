from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.level + " " + self.style + " - " + self.title

class Practice(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    notes = models.CharField(max_length=700, blank=True, null=True)
    teachings = models.ManyToManyField(Lesson, through='Teaches', through_fields=('practice', 'lesson'))
    def __str__(self):
        date_string = self.date.strftime("%b %d, %Y")
        return date_string + " - " + self.overview

class Teaches(models.Model):
    practice = models.ForeignKey(Practice)
    lesson = models.ForeignKey(Lesson)
    notes = models.CharField(max_length=200, blank=True, null=True)
