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

class Level(models.Model):
    name = models.CharField(max_length=200)
    position = models.IntegerField()
    def __str__(self):
        return self.name

class Lesson(models.Model):
    # first in tuple stored in database and used as title in admin table,
    # second displayed in admin drop down
    Style_CHOICES = (
        ('On1 Salsa', 'On1 Salsa'),
        ('On2 Salsa', 'On2 Salsa'),
        ('Bachata', 'Bachata'),
        ('On2 Cha Cha', 'On2 Cha Cha'),
        ('Rueda', 'Rueda'),
    )
    title = models.CharField(max_length=200)
    level = models.ForeignKey(Level, default = 1)
    style = models.CharField(max_length=200, choices=Style_CHOICES, blank=True)
    content = models.TextField()
    def __str__(self):
        name = ""
        if (self.level.name != ""):
            name += self.level.name + " "
        if (self.style != ""):
            name += self.style + " "
        if (name != ""):
            name += "- "
        name += self.title
        return name
    class Meta:
        ordering = ['style', 'level', ]

class Practice(models.Model):
    SCHEDULED = 'S'
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = (
        (SCHEDULED, 'Scheduled'),
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    MONDAY_PRACTICE = 'MP'
    OFFICE_HOURS = 'OH'
    GUEST_LESSON = 'GL'
    OTHER = 'O'
    TYPE_CHOICES = (
        (MONDAY_PRACTICE, 'Monday Practice'),
        (OFFICE_HOURS, 'Office Hours'),
        (GUEST_LESSON, 'Guest Lesson'),
        (OTHER, 'Other'),
    )

    overview = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=DRAFT)
    practice_type = models.CharField(max_length=200, choices=TYPE_CHOICES, default=MONDAY_PRACTICE)
    notes = models.CharField(max_length=700, blank=True, null=True)
    timing_and_music_1 = models.ForeignKey(Instructor, related_name="timing_1", blank=True, null=True, limit_choices_to={'is_active': True})
    timing_and_music_2 = models.ForeignKey(Instructor, related_name="timing_2", blank=True, null=True, limit_choices_to={'is_active': True})
    teachings = models.ManyToManyField(Lesson, through='Teaches', through_fields=('practice', 'lesson'))
    class Meta:
        ordering = ['date']
    def __str__(self):
        date_string = self.date.strftime("%b %d, %Y")
        return date_string + " - " + self.overview

class Teaches(models.Model):
    practice = models.ForeignKey(Practice)
    lesson = models.ForeignKey(Lesson)
    lead_instructor = models.ForeignKey(Instructor, related_name="teaches_lead", blank=True, null=True, limit_choices_to={'is_active': True, 'is_lead': True})
    follow_instructor = models.ForeignKey(Instructor, related_name="teaches_follow", blank=True, null=True, limit_choices_to={'is_active': True, 'is_follow': True})
    additional_instructor = models.ForeignKey(Instructor, related_name="teaches_additional", blank=True, null=True, limit_choices_to={'is_active': True})
    notes = models.CharField(max_length=200, blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    class Meta:
        verbose_name = "assignment"
        ordering = ['hour']
    def __str__(self):
        return "Lesson Assignment"
