from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('get_projects'))
    else:
        return redirect(reverse('login'))