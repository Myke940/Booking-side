from django.shortcuts import render, redirect
from .models import Problem, Meeting
from datetime import datetime as d
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


def logout_user(request):
    logout(request)
    return redirect('problemslist')

def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request = request, template_name = 'login.html', context = {'form' : form})
    else:
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request = request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('problemslist')
            
            else:
                return render(request = request, template_name = 'login.html', context = {'form' : form})
        else:
            return render(request = request, template_name = 'login.html', context = {'form' : form})

def register_user(request):
    if request.method == 'GET':
        form =  UserCreationForm()
        return render(request = request, template_name = 'register.html', context = {'form' : form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('problemslist')
        else:
            return render(request = request, template_name = 'register.html', context = {'form' : form})


def problemslist(request):
    problems = Problem.objects.all()
    


    if request.method == 'POST':
        category = request.POST.get('category')
        problems = problems.filter(categoryofproblem = category)
    context = {'problems' : problems}
    return render(request = request, template_name = 'problems_list.html', context = context)
@login_required
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