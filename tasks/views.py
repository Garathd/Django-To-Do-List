from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task
from projects.models import Project
from .forms import TaskForm
from django.utils import timezone
        
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
    
    if project != None:
        project_instance = get_object_or_404(Project, pk=project)

    task = get_object_or_404(Task, pk=pk) if pk else None
   
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if project != None:
                task.project = project_instance
            task.save()
            return redirect(reverse('get_projects'))
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

        