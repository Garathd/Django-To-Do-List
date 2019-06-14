from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task
from projects.models import Project
from .forms import TaskForm
from django.utils import timezone
from accounts.models import UserProfile
        
@login_required()
#Get Task Information
def task_info(request, project, pk):
    
    task = get_object_or_404(Task, pk=pk)
    task.save()

    return render(request, "taskinfo.html", {
        'task': task,
        'project': project
    })


@login_required() 
#Create or Edit a Task
def create_or_edit_task(request, pk=None, project=None):
    
    
    project_info = Project.objects.filter(id=project)
    tasks = Task.objects.filter(project=project)
    
    for pi in project_info:
        project_id = pi.id
        project_name = pi.name
    
    info = UserProfile.objects.filter(user=request.user)
    for i in info:
        account_type = i.account
    
    if project != None:
        project_instance = get_object_or_404(Project, pk=project)

    task = get_object_or_404(Task, pk=pk) if pk else None
    
    task_count = Task.objects.filter(project=project).count()
    
    if request.method == "POST":
        
        if account_type == "free" and task_count >= 3 and pk == None:

            return render(request, "project_tasks.html", {
                'tasks': tasks,
                'project_id': project_id,
                'project': project_name,
                'result': "trial"
            })
            
        else:

            form = TaskForm(request.POST, request.FILES, instance=task)
            if form.is_valid():
                task = form.save(commit=False)
                if project != None:
                    task.project = project_instance
                task.save()
                return redirect(reverse('task_info', kwargs={
                    'project': project,
                    'pk': task.id 
                }))
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskform.html', {
        'form': form,
        'task': pk,
        'project': project
    })

    
@login_required()     
#Deletes a Task    
def delete_task(request, pk=None):
    
    Task.objects.filter(id=pk).delete()
    return redirect(reverse('get_projects'))

        