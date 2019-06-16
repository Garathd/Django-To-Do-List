from django.test import TestCase, Client
from accounts.client import Login


"""
Checks the if the cart page redirects because the cart is empty
"""
class CartViewTests(TestCase):

    def test_cart_view(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 302)

        