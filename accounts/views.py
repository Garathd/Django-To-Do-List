from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile, create_or_update_user_profile
from accounts.forms import UserProfileForm

from projects.models import Project
from tasks.models import Task


"""
A view that logs the user out and redirects back to the index page
"""
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


"""
A view that manages the login form
"""
def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('dashboard'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


"""
A view that shows the profile and requires a user to be logged in
"""
@login_required
def profile(request):

    # Get data for logged in user
    info = UserProfile.objects.filter(user=request.user)
    
    # Get projects for current user
    projects = Project.objects.filter(user__username=request.user)

    # Calculate the total projects and tasks for logged in user
    project_count = 0
    task_count = 0

    for p in projects:
        task = Task.objects.filter(project=p).count()
        project_count = project_count + 1
        task_count = task_count + task

    return render(request, 'profile.html', {
        'info': info,
        'project_count': project_count,
        'task_count': task_count
    })


"""
A view that lets a user edit their profile
"""
def edit_profile(request, pk=None):

    # Get user profile details
    profile = get_object_or_404(UserProfile, user=request.user) 
    
    info = UserProfile.objects.filter(user=request.user)
    for i in info:
        username = i.user

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profileform.html', {
        'form': form,
        'username': username
    })


"""
A view that manages the registration form
"""
def register(request):
 
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)

