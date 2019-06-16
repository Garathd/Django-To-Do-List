from django.test import TestCase, Client
from accounts.client import Login

# Create your tests here.
class CartViewTest(TestCase):
    
    # This runs a testing client
    c = Client()
    
    def test_cart_view(self):
        Login.setUp(self)
        page = self.c.get("/cart/")
        # Checking to see if page redirects because cart is empty
        self.assertEqual(page.status_code, 302)


 