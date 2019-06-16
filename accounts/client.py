from django.test import Client
from .forms import UserRegistrationForm

class Login:
    
    c = Client()

    def setUp(self):

        user = UserRegistrationForm({"username":"test", "email":"test@test.com", "password1":"access", "password2":"access"})
        this_user = user.save()
        logged_in = self.c.login(username='test', password='access')
        
        def __str__(self):
            return self.name