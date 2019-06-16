from django.test import TestCase, Client
from accounts.client import Login


"""
Checks the if logged in user can access the dashboard page
"""
class DashboardViewTests(TestCase):
    
    # This runs a testing client
    c=Client()
    
    def test_dashboard_view(self):
        Login.setUp(self)
        page = self.c.get("/dashboard/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboard.html")