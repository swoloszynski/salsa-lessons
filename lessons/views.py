from django.shortcuts import render
from django.http import HttpResponse
from lessons.models import Practice, Lesson

def index(request):
    upcoming_practice_list = Practice.objects.all() #order_by('-date')[:5]
    output = ', '.join([p.overview for p in upcoming_practice_list])
    return HttpResponse(output)
