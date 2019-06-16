from django.shortcuts import render, redirect, reverse


"""
View the Cart
"""
def view_cart(request):
    
    cart = request.session.get('cart')
    
    # If cart is empty the redirect to profile page
    if not cart:
        return redirect(reverse('profile'))
    
    """A View that renders the cart contents page"""
    return render(request, "cart.html")
    
    
"""
Add a quantity of the specified product to the cart
"""
def add_to_cart(request, id):
    
    
    cart = request.session.get('cart')
    
    # This code stops users from using the back button to add more to cart
    if cart:
        first = cart['1']
        if first >= 1:
            return redirect(reverse('products'))
    
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('checkout'))


"""
Adjust the quantity of the specified product to the specified
amount. I have it to set to 0 if a user delete which is only 
way to adjust
"""
def adjust_cart(request, id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('profile'))