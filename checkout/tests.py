from django.test import TestCase, Client
from accounts.client import Login
from .forms import OrderForm, MakePaymentForm
from .models import Order


"""
Checks the if the checkout page redirects because the cart is empty
"""
class CheckoutViewTests(TestCase):

    def test_checkout_view(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)


"""
Testing the Checkout Order Form
"""
class CheckoutFormTests(TestCase):
    
    def test_order_form(self):

        form = OrderForm({
            'full_name': 'Example User',
            'phone_number': '089 1122334',
            'country': 'Ireland',
            'postcode': 'EA1 3021',
            'town_or_city': 'Galway',
            'street_address1': 'Merlin Park',
            'street_address2': 'Renmore',
            'county': 'Galway'
        })
        self.assertTrue(form.is_valid())
        

"""
Testing the Checkout Model
"""
class CheckoutModelTests(TestCase):
    
    def test_order_model(self):
        order = Order(
            full_name = 'Example User',
            phone_number = '089 1122334',
            country = 'Ireland',
            postcode = 'EA1 3021',
            town_or_city = 'Galway',
            street_address1 = 'Merlin Park',
            street_address2 = 'Renmore',
            county = 'Galway',
            date = '2020-12-31'
        )
        order.save()
        self.assertEqual(order.full_name, "Example User")
        self.assertEqual(order.phone_number, "089 1122334")
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.postcode, "EA1 3021")
        self.assertEqual(order.town_or_city, "Galway")
        self.assertEqual(order.street_address1, "Merlin Park")
        self.assertEqual(order.street_address2, "Renmore")
        self.assertEqual(order.county, "Galway")
        self.assertEqual(order.date, "2020-12-31")
        