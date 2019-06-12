from django.shortcuts import render, redirect, reverse
from .models import Product
from accounts.models import UserProfile

# Create your views here.
def all_products(request):
    
    # Make sure pro version product not added again
    added = False
    
    cart = request.session.get('cart')    
    if cart:
        added = True

    user_info = UserProfile.objects.filter(user=request.user)
    
    for u in user_info:
        account = u.account
    
    products = Product.objects.all()
    return render(request, "products.html", {
        "products": products,
        "account": account,
        "added": added
    })