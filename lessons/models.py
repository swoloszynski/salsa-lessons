from django.db import models

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
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    overview = models.CharField(max_length=200)
    notes = models.CharField(max_length=700, blank=True, null=True)
    teachings = models.ManyToManyField(Lesson, through='Teaches', through_fields=('practice', 'lesson'))
    def __str__(self):
        date_string = self.date.strftime("%b %d, %Y")
        return date_string + " - " + self.overview

class Instructor(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    year = models.IntegerField()
    # TODO add phone validation
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    isLead = models.BooleanField(default=False)
    isFollow = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    notes = models.TextField()
    def __str__(self):
        return self.first + " " + self.last

class Teaches(models.Model):
    practice = models.ForeignKey(Practice)
    lesson = models.ForeignKey(Lesson)
    notes = models.CharField(max_length=200, blank=True, null=True)
