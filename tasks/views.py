from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task
from projects.models import Project
from .forms import TaskForm
from django.utils import timezone
from accounts.models import UserProfile


@login_required() 
#Create or Edit a Task
def create_or_edit_task(request, pk=None, project=None):
    
    project_info = Project.objects.filter(id=project)
    
    # This is to prevent another user accessing another users data
    for pi in project_info:
        user_name = pi.user
        if user_name != request.user:
            return redirect(reverse('get_projects'))

    
    tasks = Task.objects.filter(project=project)
    tasks = Task.objects.filter(project=project,pk=pk)
    
    task_name = False
    for ti in tasks:
        task_name = ti.name

    
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
                return redirect(reverse('view_only', kwargs={
                    'pk': project_id
                }))
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskform.html', {
        'form': form,
        'task': pk,
        'project': project,
        'project_name': project_name,
        'project_id': project_id,
        'task_name': task_name
    })

    
@login_required()     
#Deletes a Task    
def delete_task(request, pk=None):
    
    get_project = Task.objects.filter(id=pk)
    
    for pi in get_project:
        project = Project.objects.filter(name=pi.project)
        for pj in project:
            project_id = pj.id
    
    Task.objects.filter(id=pk).delete()
    
    return redirect(reverse('view_only', kwargs={
                    'pk': project_id
                }))

        