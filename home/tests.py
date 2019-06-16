from django.test import TestCase, Client
from accounts.client import Login


"""
Test the Home View for a user being signed in or not signed in
"""
class HomeViewTests(TestCase):
    
    # This runs a testing client
    c = Client()
    
    # Logged In 
    def test_home_logged_in_view(self):
        Login.setUp(self)
        page = self.c.get("/dashboard/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboard.html")
        
    
    # Not Logged In
    def test_home_not_logged_in_view(self):
        page = self.client.get("/dashboard/")
        self.assertEqual(page.status_code, 302)
        self.assertTemplateNotUsed(page, "dashboard.html")