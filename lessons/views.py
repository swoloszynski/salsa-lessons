from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from lessons.models import Practice, Lesson

def index(request):
    upcoming_practice_list = Practice.objects.all() #order_by('-date')[:5]
    template = loader.get_template('lessons/index.html')
    context = RequestContext(request, {
        'upcoming_practice_list': upcoming_practice_list,
    })
    return HttpResponse(template.render(context))
