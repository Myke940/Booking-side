from django.shortcuts import render, redirect
from .models import Problem, Meeting
from datetime import datetime as d
from django.urls import reverse
from django.utils.dateparse import parse_datetime
def problemslist(request):
    problems = Problem.objects.all()
    
    if request.method == 'POST':
        category = request.POST.get('category')
        problems = problems.filter(categoryofproblem = category)
    context = {'problems' : problems}
    return render(request = request, template_name = 'problems_list.html', context = context)

def bookmeeting(request):
    if request.method == 'GET':
        problem_id = request.GET.get('problemid')
        problem = Problem.objects.get(id = problem_id)
        context = {'problem' : problem}
        return render(request = request, template_name = 'problem.html', context = context)
    elif request.method == 'POST':
        problem_id = request.POST.get('problem_id')
        datetime = request.POST.get('datetime')
        datetime = d.fromisoformat(datetime)
        problem = Problem.objects.get(id = problem_id)
        currenttime = d.now()
        if datetime <= currenttime:
            return redirect(reverse('bm') + f'?problemid={problem_id}')

        meet = Meeting.objects.create(user = request.user, usedproblem = problem, datetimemeet = datetime)
        return redirect('problemslist')
    
def meetinghistory(request):
    meetings = Meeting.objects.filter(user = request.user).order_by('-time')
    return render(request = request, template_name = 'history.html', context = {'Meetings' : meetings})