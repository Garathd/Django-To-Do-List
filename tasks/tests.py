from django.utils import timezone
from django.test import TestCase, Client
from accounts.client import Login
from .forms import TaskForm
from .models import Project
from .models import Task


"""
Tests for all the task forms        
"""
class TaskFormTests(TestCase):
    
    def test_task_form(self):
        
        form = TaskForm({
            'name': 'Task', 
            'description': 'example description',
            'status': 'To Do',
            'priority': 'High',
            'screenshot': ''
            
        })
        self.assertTrue(form.is_valid())
        
    
"""
Tests for all the task Models        
"""    
class TaskModelsTests(TestCase):
    
    c = Client()
    
    def test_task_model(self):
        
        current_time = timezone.now()
    
        # Creating a project
        project = Project(
            name = "Project",
            description = "Example Description",
            status = "Work",
            user = Login.setUp(self),
            user_id = 1,
            published_date = current_time
        )
        
        project.save()
        
        
        # Creating a task
        task = Task(
            name = "Task",
            description = "Example Description",
            project = project,
            status = "To Do",
            priority = "High",
            screenshot = "",
            published_date = current_time
        )
        
        task.save()
        
        self.assertEqual(task.name, "Task")
        self.assertEqual(task.description, "Example Description")
        self.assertEqual(task.status, "To Do")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.published_date, current_time)
        

"""
Tests for all the task Views        
"""    
class TaskViewTests(TestCase):
    
    c = Client()
    
    def test_view_task_info(self):
        
        current_time = timezone.now()
        
        # Creating a project
        project = Project(
            name = "Project",
            description = "Example Description",
            status = "Work",
            user = Login.setUp(self),
            user_id = 1,
            published_date = current_time
        )
        
        project.save()
        
        # Creating a task
        task = Task(
            name = "Task",
            description = "Example Description",
            project = project,
            status = "To Do",
            priority = "High",
            screenshot = "",
            published_date = current_time
        )
        
        task.save()

        page = self.c.get("/tasks/{0}/project/{1}/".format(task.id,project.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "taskinfo.html")