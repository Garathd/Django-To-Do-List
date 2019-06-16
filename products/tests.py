from django.test import TestCase, Client
from .models import Product
from accounts.client import Login


"""
Test the Product View
"""
class ProductViewTest(TestCase):
    
    # This runs a testing client
    c = Client()

    def test_all_products(self):
        Login.setUp(self)
        page = self.c.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
    
    
"""
Test the Product Model
"""
class ProductModelTests(TestCase):

    def test_product_model(self):
        
        product = Product(
            name = 'Product',
            description = 'Example Description',
            price = '1.99'    
        )
        product.save()
        
        self.assertEqual(product.name, 'Product')
        self.assertEqual(product.description, 'Example Description')
        self.assertEqual(product.price, '1.99')