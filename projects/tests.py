from django.utils import timezone
from django.test import TestCase, Client, RequestFactory
from .forms import ProjectForm
from .models import Project
from accounts.client import Login
from django.contrib.auth.models import User


"""
Tests for all the project forms
"""
class ProjectFormTests(TestCase):

    # This runs a testing client
    c = Client()
    
    # Testing project form
    def test_project_form(self):
        Login.setUp(self)
        form = ProjectForm({
            'name': 'example project', 
            'description': 'example description',
            'status': 'Work'
        })
        self.assertTrue(form.is_valid())
        

"""
Tests for all the projects models
"""
class ProjectModelTests(TestCase):
    
    c = Client()
    
    def test_project_model(self):
    
        current_time = timezone.now()
    
        project = Project(
            name = "Project",
            description = "Example Description",
            status = "Work",
            user = Login.setUp(self),
            user_id = 1,
            published_date = current_time
        )
        project.save()
        self.assertEqual(project.name, "Project")
        self.assertEqual(project.description, "Example Description")
        self.assertEqual(project.status, "Work")
        self.assertEqual(project.user_id, 1)
        self.assertEqual(project.published_date, current_time)


"""
Tests for all the project views
"""
class ProjectViewTests(TestCase):
    
    # This runs a testing client
    c=Client()
    
    # Testing the get products view  
    def test_get_projects_view(self):
        Login.setUp(self)
        page = self.c.get("/projects/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "projects.html")
        
        
    # Testing the project info view
    def test_project_info_view(self):
        
        current_time = timezone.now()
        
        project = Project(
            name = "Project",
            description = "Example Description",
            status = "Work",
            user = Login.setUp(self),
            user_id = 1,
            published_date = current_time
        )
        
        project.save()

        page = self.c.get("/projects/{}/".format(project.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "projectinfo.html")
        
        
    # Testing the view only tasks by specific project id
    def test_view_only_project_view(self):
        
        current_time = timezone.now()
        
        project = Project(
            name = "Project",
            description = "Example Description",
            status = "Work",
            user = Login.setUp(self),
            user_id = 1,
            published_date = current_time
        )
        
        project.save()

        page = self.c.get("/projects/{}/view/".format(project.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "project_tasks.html")
        
    