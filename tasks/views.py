from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task
from projects.models import Project
from .forms import TaskForm
from django.utils import timezone

# login_required()
# #Get all Projects
# def get_tasks(request):

#     #Check if user used the select option
#     if request.method == "POST":

#         """ 
#         This is for the filtered select option
#         on the tasks page
#         """
#         search_select = request.POST['search']
        
#         if search_select == 'all':
#             tasks = Task.objects.filter(project__user=request.user)

#         if search_select == 'hpriority':
#             tasks = Task.objects.filter(priority='High', project__user=request.user)

#         if search_select == 'mpriority':
#             tasks = Task.objects.filter(priority='Medium', project__user=request.user)

#         if search_select == 'lpriority':
#             tasks = Task.objects.filter(priority='Low', project__user=request.user)

#         if search_select == 'todo':
#             tasks = Task.objects.filter(status='To Do', project__user=request.user)
            
#         if search_select == 'progress':
#             tasks = Task.objects.filter(status='In Progress', project__user=request.user)
            
#         if search_select == 'done':
#             tasks = Task.objects.filter(status='Done', project__user=request.user)
        
#         """ 
#         What ever is choosen in the select box 
#         is no filtered and resend to tasks page
#         """
#         return render(request, "tasks.html", {'tasks': tasks})
        
#     else:
#         tasks = Task.objects.filter(project__user=request.user)
#         return render(request, "tasks.html", {'tasks': tasks})
        
        
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
    return render(request, 'taskform.html', {'form': form})

    
@login_required()     
#Deletes a Task    
def delete_task(request, pk=None):
    
    Task.objects.filter(id=pk).delete()
    return redirect(reverse('get_projects'))

        