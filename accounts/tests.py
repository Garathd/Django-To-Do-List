from django.test import TestCase, Client
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import UserProfile
from .client import Login

# Tests for all the accounts forms
class AccountFormTests(TestCase):

    # Testing account login form
    def test_account_login_form(self):
        form = UserLoginForm({
            'username_or_email': 'example user', 
            'password': 'example password'
        })
        self.assertTrue(form.is_valid())
        
        
    # Testing account registration form
    def test_account_registration_form(self):
        form = UserRegistrationForm({
            'username': 'user', 
            'email': 'test@test.com',
            'password1': 'xxxxx',
            'password2': 'xxxxx'
            
        })
        self.assertTrue(form.is_valid())
        
        
    # Testing the user profile form
    def test_user_profile_form(self):
        form = UserProfileForm({
            'description': 'testing',
            'picture': False
        })
        self.assertTrue(form.is_valid())
        

# Tests for all the accounts models        
class AccountModelTests(TestCase):
    
    # Testing the user profile model
    def test_user_profile_model(self):
        profile = UserProfile(
            user_id = "1",
            description = "Example Description"
        )
        profile.save()
        self.assertEqual(profile.description, "Example Description")
        

# Tests for all the accounts views          
class AccountViewTests(TestCase):
    
    # This runs a testing client
    c=Client()
    
    # Testing the register view  
    def test_register_view(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
        
        
    # Testing the login view  
    def test_login_view(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
        
    # Testing the profile view  
    def test_profile_view(self):
        Login.setUp(self)
        page = self.c.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    
     # Testing the profile view  
    def test_edit_profile_view(self):
        Login.setUp(self)
        page = self.c.get("/accounts/edit_profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profileform.html")
