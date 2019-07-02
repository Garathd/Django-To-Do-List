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
    
    # Get project information
    project_info = Project.objects.filter(id=project)
    
    # This is to prevent another user accessing another users data
    for pi in project_info:
        user_name = pi.user
        if user_name != request.user:
            return redirect(reverse('get_projects'))

    tasks = Task.objects.filter(project=project,pk=pk)
    
    # If new task set task_name to false
    task_name = False
    
    # Getting the task name
    for ti in tasks:
        task_name = ti.name

    # Getting project name and id
    for pi in project_info:
        project_id = pi.id
        project_name = pi.name
    
    # Getting user profile information
    info = UserProfile.objects.filter(user=request.user)
    
    # Seeing if the user account is pro or trial version
    for i in info:
        account_type = i.account
    
    if project != None:
        project_instance = get_object_or_404(Project, pk=project)

    # Setting task information for new or edit task
    task = get_object_or_404(Task, pk=pk) if pk else None
    
    # Counting how many tasks have been created for current project
    task_count = Task.objects.filter(project=project).count()
    
    # Checking if the form has been posted
    if request.method == "POST":
        
        # Checking if the user has a trial account to ensure no more than 3 tasks are created
        if account_type == "free" and task_count >= 3 and pk == None:
        
            return render(request, "project_tasks.html", {
                'tasks': tasks,
                'project_id': project_id,
                'project': project_name,
                'task_type': "Trial",
                'result': "trial"
            })
         
        # This is if a trial user has less than 3 tasks and also this is used for the pro version       
        else:

            form = TaskForm(request.POST, request.FILES, instance=task)
            if form.is_valid():
                task = form.save(commit=False)
                if project != None:
                    
                    # Set the project
                    task.project = project_instance
                    
                task.save()
                return redirect(reverse('view_only', kwargs={
                    'pk': project_id
                }))
    
    # The form has not been posted             
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
    
    # This is to get project ID information for redirect
    get_project = Task.objects.filter(id=pk)
    for pi in get_project:
        project = Project.objects.filter(name=pi.project)
        for pj in project:
            project_id = pj.id
    
    Task.objects.filter(id=pk).delete()
    
    return redirect(reverse('view_only', kwargs={
                    'pk': project_id
                }))

        