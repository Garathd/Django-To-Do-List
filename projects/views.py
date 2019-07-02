from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.urlresolvers import resolve
from django.contrib.auth.decorators import login_required
from .models import Project
from tasks.models import Task
from accounts.models import UserProfile
from .forms import ProjectForm

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

        # Checks if the Show All Select Option was Choosen
        if search_select == 'all':
            projects = Project.objects.filter(user__username=request.user)
            project_type = "Show All"
        
        # Checks if the Work Select Option was Choosen
        if search_select == 'work':
            projects = Project.objects.filter(status='Work', user__username=request.user)
            project_type = "Work"

        # Checks if the Education Select Option was Choosen
        if search_select == 'education':
            projects = Project.objects.filter(status='Education', user__username=request.user)
            project_type = "Education"
            
        # Checks if the Personal Select Option was Choosen
        if search_select == 'personal':
            projects = Project.objects.filter(status='Personal', user__username=request.user)
            project_type = "Personal"
        
        # Count the amount of projects a user has
        project_count = Project.objects.filter(user__username=request.user).count()
            
        """ 
        What ever is choosen in the select box 
        is now filtered and resend to projects page
        """
        return render(request, "projects.html", {
            'projects': projects,
            'project_count': project_count,
            'project_type': project_type
        })
        
    else:
        
        # Getting all the users projects
        projects = Project.objects.filter(user__username=request.user)
        
        # Count the amount of projects a user has
        project_count = Project.objects.filter(user__username=request.user).count()
        
        # Set Show All as the default select option
        project_type = "Show All"
        
        return render(request, "projects.html", {
            'projects': projects,
            'project_count': project_count,
            'project_type': project_type
        })
        
        
@login_required()    
#Get Project Information
def project_info(request, pk):
    
    # Get Project Information
    project = get_object_or_404(Project, pk=pk)
    project.save()
    
    # This is to prevent another user accessing another users data
    project_info = Project.objects.filter(pk=pk)
    for pi in project_info:
        project_user = pi.user
        
    # Checks if the users are not the same
    if project_user != request.user:
        return redirect(reverse('get_projects'))

    # Get User Profile Information
    user_info = UserProfile.objects.filter(user=request.user)
    
    # Getting Project Picture
    for u in user_info:
        picture = u.picture
    
    return render(request, "projectinfo.html", {
        'project': project,
        'picture': picture
    })
    
@login_required()  
#Edit or Create a Project
def create_or_edit_project(request, pk=None):

    # Default parameters
    project_count = 0
    account_type = ""
    
    # Checking if there is an associated project id (Editing)
    if pk:
        project_info = Project.objects.filter(user__username=request.user, pk=pk)
        
        # Makes sure the project belongs to the user
        if project_info:
            for pi in project_info:
                # Get the project name
                project_name = pi.name
                
        # If user tries to access another users project the gets send back to project page
        else: 
           return redirect(reverse('get_projects'))
     
    # No project id means this is a new project   
    else:
        project_name = False
    
    # Get the users information and checking if the account is a trial or is a pro version
    info = UserProfile.objects.filter(user=request.user)
    for i in info:
        account_type = i.account
        
    # Count how many projects the user has    
    projects = Project.objects.filter(user__username=request.user)
    for p in projects:
        project_count = project_count + 1

    project = get_object_or_404(Project, pk=pk) if pk else None
    
    # Checking if the form has been posted
    if request.method == "POST":

        # Checking if the user has a trial account to ensure no more than 1 project is created
        if account_type == "free" and project_count >= 1 and pk == None:

            return render(request,'projects.html',{
                'projects': projects,
                'result': "trial"
            })
            
        # This is if a trial user has less than 1 project and also this is used for the pro version    
        else:
            
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                
                # Set the user for the project 
                project.user = request.user
                
                project.save()
                return redirect(reverse('project_info', 
                kwargs={
                    'pk': project.id
                }))
    
    # The form has not been posted            
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
    
    # Delete a project by id
    Project.objects.filter(id=pk).delete()
    return redirect(reverse('get_projects'))
    

@login_required()
#Selects tasks for a specific project only
def view_only(request, pk=None):

    # Getting project information
    project = Project.objects.filter(id=pk)
    
    # This is to prevent another user accessing another users data
    for pi in project:
        user_name = pi.user
        if user_name != request.user:
            return redirect(reverse('get_projects'))
    
    # Getting task information for associated project
    tasks = Task.objects.filter(project=project)
    
    # Setting the project name
    for p in project:
        project_name = p.name
        
    #Check if user used the select option
    if request.method == "POST":

        """ 
        This is for the filtered select option
        on the tasks page
        """
        search_select = request.POST['search']
        
        # Checks if the Show All Select Option was Choosen
        if search_select == 'all':
            tasks = Task.objects.filter(project=project)
            task_type = "Show All"
            
        # Checks if the High Priority Select Option was Choosen
        if search_select == 'hpriority':
            tasks = Task.objects.filter(priority='High', project=project)
            task_type = "High Priority"

        # Checks if the Medium Priority Select Option was Choosen
        if search_select == 'mpriority':
            tasks = Task.objects.filter(priority='Medium', project=project)
            task_type = "Medium Priority"

        # Checks if the Low Priority Select Option was Choosen
        if search_select == 'lpriority':
            tasks = Task.objects.filter(priority='Low', project=project)
            task_type = "Low Priority"

        # Checks if the To DO Select Option was Choosen
        if search_select == 'todo':
            tasks = Task.objects.filter(status='To Do', project=project)
            task_type = "To Do"

        # Checks if the In Progress Select Option was Choosen
        if search_select == 'progress':
            tasks = Task.objects.filter(status='In Progress', project=project)
            task_type = "In Progress"

        # Checks if the Done Select Option was Choosen
        if search_select == 'done':
            tasks = Task.objects.filter(status='Done', project=project)
            task_type = "Done"
            
        # Getting the task count for associated project
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
        #Get all tasks from associated project
        tasks = Task.objects.filter(project=project)
        
        # Set default select option
        task_type = "Show All"
        
        # Count the amount of tasks for associated
        task_count = Task.objects.filter(project=project).count()
        
        return render(request, "project_tasks.html", {
            'tasks': tasks,
            'project_id': pk,
            'project': project_name,
            'task_type': task_type,
            'task_count': task_count
        })    

