from django.shortcuts import render, redirect, reverse

"""
This view is to determine a redirect based on a user being signed in or not signed in
"""
def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('dashboard'))
    else:
        return redirect(reverse('login'))