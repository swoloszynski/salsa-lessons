from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from lessons.models import Practice, Lesson, Teaches, Instructor

def index(request):
    upcoming_practice_list = Practice.objects.order_by('date')
    context = {'upcoming_practice_list': upcoming_practice_list}
    return render(request, 'lessons/index.html', context)

def practice_detail(request, practice_id):
    practice = get_object_or_404(Practice, pk=practice_id)
    assignments = practice.teaches_set.order_by('hour')
    context = {
      'practice': practice,
      'assignments': assignments
    }
    return render(request, 'lessons/practice_detail.html', context)

def instructors(request):
    instructors = Instructor.objects.exclude(is_active=False)
    assignments = Teaches.objects.order_by('-practice')
    practices = Practice.objects.all()
    context = {'instructors': instructors, 'assignments': assignments, 'practices': practices}
    return render(request, 'lessons/instructors.html', context)
