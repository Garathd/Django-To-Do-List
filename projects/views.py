from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Project

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
        
        if search_select == 'work':
            projects = Project.objects.filter(status='Work', user__username=request.user)

        if search_select == 'education':
            projects = Project.objects.filter(status='Education', user__username=request.user)
            
        if search_select == 'personal':
            projects = Project.objects.filter(status='Personal', user__username=request.user)
            
        """ 
        What ever is choosen in the select box 
        is no filtered and resend to tasks page
        """
        return render(request, "projects.html", {'projects': projects})
        
    else:
        projects = Project.objects.filter(user__username=request.user)
        
        return render(request, "projects.html", {'projects': projects})