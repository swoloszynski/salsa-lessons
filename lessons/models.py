from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.ForeignKey(User, unique=True)
    year = models.IntegerField()
    # TODO add phone validation
    phone = models.CharField(max_length=15)
    is_lead = models.BooleanField(default=False, verbose_name="lead")
    is_follow = models.BooleanField(default=False, verbose_name="follow")
    is_active = models.BooleanField(default=True, verbose_name="active")
    notes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.first_name

class Lesson(models.Model):
    # first in tuple stored in database and used as title in admin table,
    # second displayed in admin drop down
    LEVEL_CHOICES = (
        ('Intro', 'Intro'),
        ('Beginner', 'Beginner'),
        ('Accelerated Beginner', 'Accelerated Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    Style_CHOICES = (
        ('On1 Salsa', 'On1 Salsa'),
        ('On2 Salsa', 'On2 Salsa'),
        ('Bachata', 'Bachata'),
        ('On2 Cha Cha', 'On2 Cha Cha'),
        ('Rueda', 'Rueda'),
    )
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=200, choices=LEVEL_CHOICES, blank=True)
    style = models.CharField(max_length=200, choices=Style_CHOICES, blank=True)
    content = models.TextField()
    def __str__(self):
        name = ""
        if (self.level != ""):
            name += self.level + " "
        if (self.style != ""):
            name += self.style + " "
        if (name != ""):
            name += "- "
        name += self.title
        return name

class Practice(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    overview = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=DRAFT)
    notes = models.CharField(max_length=700, blank=True, null=True)
    timing_and_music_1 = models.ForeignKey(Instructor, related_name="timing_1", blank=True, null=True, limit_choices_to={'is_active': True})
    timing_and_music_2 = models.ForeignKey(Instructor, related_name="timing_2", blank=True, null=True, limit_choices_to={'is_active': True})
    teachings = models.ManyToManyField(Lesson, through='Teaches', through_fields=('practice', 'lesson'))
    def __str__(self):
        date_string = self.date.strftime("%b %d, %Y")
        return date_string + " - " + self.overview

class Teaches(models.Model):
    practice = models.ForeignKey(Practice)
    lesson = models.ForeignKey(Lesson)
    lead_instructor = models.ForeignKey(Instructor, related_name="teaches_lead", blank=True, null=True, limit_choices_to={'is_active': True, 'is_lead': True})
    follow_instructor = models.ForeignKey(Instructor, related_name="teaches_follow", blank=True, null=True, limit_choices_to={'is_active': True, 'is_follow': True})
    notes = models.CharField(max_length=200, blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    class Meta:
        verbose_name = "assignment"
    def __str__(self):
        return "Lesson Assignment"
