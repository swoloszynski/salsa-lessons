from django.shortcuts import get_object_or_404, render, redirect
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

def instructors_leads(request):
    instructors = Instructor.objects.exclude(is_active=False).exclude(is_lead=False)
    assignments = Teaches.objects.order_by('-practice')
    practices = Practice.objects.all()
    leads = True
    context = {'instructors': instructors, 'assignments': assignments, 'practices': practices, 'leads': leads}
    return render(request, 'lessons/instructors.html', context)

def instructors_follows(request):
    instructors = Instructor.objects.exclude(is_active=False).exclude(is_follow=False)
    assignments = Teaches.objects.order_by('-practice')
    practices = Practice.objects.all()
    follows = True
    context = {'instructors': instructors, 'assignments': assignments, 'practices': practices, 'follows': follows}
    return render(request, 'lessons/instructors.html', context)

def instructors(request):
    return redirect('instructors_leads')
