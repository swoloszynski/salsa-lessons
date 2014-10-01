from django.shortcuts import render
from django.http import HttpResponse
from lessons.models import Practice, Lesson

def index(request):
    upcoming_practice_list = Practice.objects.all() #order_by('-date')[:5]
    context = {'upcoming_practice_list': upcoming_practice_list}
    return render(request, 'lessons/index.html', context)
