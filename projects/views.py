from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.urlresolvers import resolve
from django.contrib.auth.decorators import login_required
from .models import Project
from tasks.models import Task
from accounts.models import UserProfile
from .forms import ProjectForm

# Create your views here.
@login_required()
#Get all Projects
def get_projects(request):
    
       #Check if user used the select option
    if request.method == "POST":

        """ 
        This is for the filtered select option
        on the tasks page
        """
        search_select = request.POST['search']

        if search_select == 'all':
            projects = Project.objects.filter(user__username=request.user)
            project_type = "Show All"
        
        if search_select == 'work':
            projects = Project.objects.filter(status='Work', user__username=request.user)
            project_type = "Work"

        if search_select == 'education':
            projects = Project.objects.filter(status='Education', user__username=request.user)
            project_type = "Education"
            
        if search_select == 'personal':
            projects = Project.objects.filter(status='Personal', user__username=request.user)
            project_type = "Personal"
            
            
        project_count = Project.objects.filter(user__username=request.user).count()
            
        """ 
        What ever is choosen in the select box 
        is now filtered and resend to tasks page
        """
        return render(request, "projects.html", {
            'projects': projects,
            'project_count': project_count,
            'project_type': project_type
        })
        
    else:
        projects = Project.objects.filter(user__username=request.user)
        project_count = Project.objects.filter(user__username=request.user).count()
        project_type = "Show All"
        
        return render(request, "projects.html", {
            'projects': projects,
            'project_count': project_count,
            'project_type': project_type
            
        })
        
        
@login_required()    
#Get Project Information
def project_info(request, pk):
    
    project = get_object_or_404(Project, pk=pk)
    project.save()
    
    user_info = UserProfile.objects.filter(user=request.user)
    
    for u in user_info:
        picture = u.picture
    
    return render(request, "projectinfo.html", {
        'project': project,
        'picture': picture
    })
    
@login_required()  
#Edit or Create a Project
def create_or_edit_project(request, pk=None):
    
    project_count = 0
    account_type = ""
    
    if pk:
        project_info = Project.objects.filter(user__username=request.user, pk=pk)
        for pi in project_info:
            project_name = pi.name
    else: 
        project_name = False
    
    info = UserProfile.objects.filter(user=request.user)
    for i in info:
        account_type = i.account
        
    projects = Project.objects.filter(user__username=request.user)

    for p in projects:
        project_count = project_count + 1

    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == "POST":
        
        if account_type == "free" and project_count >= 1 and pk == None:

            return render(request,'projects.html',{
                'projects': projects,
                'result': "trial"
            })
        else:
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect(reverse('project_info', 
                kwargs={
                    'pk': project.id
                }))
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projectform.html', {
        'form': form,
        'project': pk,
        'project_name': project_name
    })
    
    
@login_required()   
#Deletes a project
def delete_project(request, pk=None):
    
    Project.objects.filter(id=pk).delete()
    return redirect(reverse('get_projects'))
    

@login_required()
#Selects tasks for a specific project only
def view_only(request, pk=None):

    project = Project.objects.filter(id=pk)
    tasks = Task.objects.filter(project=project)
    
    for p in project:
        project_name = p.name
        
    #Check if user used the select option
    if request.method == "POST":

        """ 
        This is for the filtered select option
        on the tasks page
        """
        search_select = request.POST['search']
        
        if search_select == 'all':
            tasks = Task.objects.filter(project=project)
            task_type = "Show All"

        if search_select == 'hpriority':
            tasks = Task.objects.filter(priority='High', project=project)
            task_type = "High Priority"

        if search_select == 'mpriority':
            tasks = Task.objects.filter(priority='Medium', project=project)
            task_type = "Medium Priority"

        if search_select == 'lpriority':
            tasks = Task.objects.filter(priority='Low', project=project)
            task_type = "Low Priority"

        if search_select == 'todo':
            tasks = Task.objects.filter(status='To Do', project=project)
            task_type = "To Do"

        if search_select == 'progress':
            tasks = Task.objects.filter(status='In Progress', project=project)
            task_type = "In Progress"

        if search_select == 'done':
            tasks = Task.objects.filter(status='Done', project=project)
            task_type = "Done"
            
        task_count = Task.objects.filter(project=project).count()
            
        """ 
        What ever is choosen in the select box 
        is no filtered and resend to tasks page
        """
        return render(request, "project_tasks.html", {
            'tasks': tasks,
            'project_id': pk,
            'project': project_name,
            'task_type': task_type,
            'task_count': task_count
        })
        
    else:
        tasks = Task.objects.filter(project=project)
        task_type = "Show All"
        task_count = Task.objects.filter(project=project).count()
        
        return render(request, "project_tasks.html", {
            'tasks': tasks,
            'project_id': pk,
            'project': project_name,
            'task_type': task_type,
            'task_count': task_count
        })    

