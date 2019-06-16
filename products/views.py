from django.shortcuts import render, redirect, reverse
from .models import Product
from accounts.models import UserProfile


"""
View for all products
"""
def all_products(request):
    
    # Make sure pro version product not added again
    added = False
    
    cart = request.session.get('cart')    
    
    # If item in cart mark added to true
    if cart:
        added = True

    # Get user info from UserProfile Model
    user_info = UserProfile.objects.filter(user=request.user)
    
    for u in user_info:
        account = u.account
    
    # Get all Products
    products = Product.objects.all()
    
    return render(request, "products.html", {
        "products": products,
        "account": account,
        "added": added
    })