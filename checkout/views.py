from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product

from accounts.models import UserProfile, create_or_update_user_profile
from accounts.forms import UserProfileForm

import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    cart = request.session.get('cart')
    
    # If cart is empty the redirect to profile page
    if not cart:
        return redirect(reverse('profile'))
    
    if request.method=="POST":

        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid for Pro Version")
                request.session['cart'] = {}
                
                profile = get_object_or_404(UserProfile, user=request.user) 
                
                preserve_description = profile.description

                if request.method == "POST":
                    form = UserProfileForm(request.POST, request.FILES, instance=profile)
                    if form.is_valid():
                        profile = form.save(commit=False)
                        profile.description = preserve_description
                        profile.account = "pro"
                        profile.save()
                        return redirect(reverse('profile'))
                
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            