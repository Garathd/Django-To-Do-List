from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task

@login_required()
def dashboard_view(request):
    
    work = 0
    education = 0
    personal = 0
    todo = 0
    progress = 0
    done = 0
    high = 0
    medium = 0
    low = 0
    
    projects = Project.objects.filter(user__username=request.user)
    for p in projects:
        if p.status == "Work":
            work = work + 1
        if p.status == "Education":
            education = education + 1
        if p.status == "Personal":
            personal = personal + 1
        
        task = Task.objects.filter(project=p)
        print("Check the Tasks: {}".format(task))
        for t in task:
            if t.status == "To Do":
                todo = todo + 1
            if t.status == "In Progress":
                progress = progress + 1
            if t.status == "Done":
                done = done + 1
            if t.priority == "High":
                high = high + 1
            if t.priority == "Medium":
                medium = medium + 1
            if t.priority == "Low":
                low = low + 1
            
    return render(request, "dashboard.html", {
        'work': work,
        'education': education,
        'personal': personal,
        'todo': todo,
        'progress': progress,
        'done': done,
        'high': high,
        'medium': medium,
        'low': low
    })
    
    
    